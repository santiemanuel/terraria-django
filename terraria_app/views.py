from django.shortcuts import render, redirect, HttpResponse
from .models.planta import Planta
from .models.pregunta import PreguntaCuidado, RegistroCuidado, SesionCuidado, RespuestaCuidado
from .forms.registro_form import RegistroCuidadoForm
from .forms.pregunta_form import PreguntaForm
from .forms.planta_form import PlantaForm
from django.utils import timezone
from django.db import transaction
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, "home.html")

def plants(request):
    plantas = Planta.objects.all() 
    return render(request, 'plantas.html', {'plantas': plantas})

def crear_planta(request):
    if request.method == 'POST':
        form = PlantaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlantaForm()

    return render(request, 'crear_planta.html', {'form': form})

def crear_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PreguntaForm()

    return render(request, 'crear_pregunta.html', {'form': form})

def crear_registro_cuidado(request):
    if request.method == 'POST':
        form = RegistroCuidadoForm(request.POST)
        if form.is_valid():
            registro_cuidado = form.save(commit=False)
            registro_cuidado.usuario = request.user
            registro_cuidado.save()

            # Guardar el orden de las preguntas seleccionadas
            preguntas = form.cleaned_data['preguntas']
            for orden, pregunta in enumerate(preguntas, start=1):
                PreguntaCuidado.objects.create(
                    registro_cuidado=registro_cuidado,
                    pregunta=pregunta,
                    orden=orden,
                )

            return redirect('home')  # Redirigir a donde sea necesario
    else:
        form = RegistroCuidadoForm()

    return render(request, 'crear_registro_cuidado.html', {'form': form})

def registros_planta_view(request, planta_id):
    planta = Planta.objects.get(pk=planta_id)
    registros = RegistroCuidado.objects.filter(planta=planta).order_by('-fecha')
    return render(request, 'registros_planta.html', {'planta': planta, 'registros': registros})

def detalle_registro_cuidado_view(request, id):
    registro_cuidado = RegistroCuidado.objects.get(pk=id)
    sesiones = SesionCuidado.objects.filter(registro_cuidado=registro_cuidado)
    return render(request, 'detalle_registro_cuidado.html', {'registro_cuidado': registro_cuidado, 'sesiones': sesiones})

def crear_sesion_cuidado(request, registro_cuidado_id):
    registro_cuidado = RegistroCuidado.objects.get(pk=registro_cuidado_id)
    sesion = SesionCuidado.objects.create(registro_cuidado=registro_cuidado, usuario=request.user, fecha_inicio=timezone.now())
    # Redireccionar a la vista para responder las preguntas de la sesión
    return redirect('responder_preguntas', sesion_cuidado_id=sesion.id)

def responder_preguntas(request, sesion_cuidado_id):
    sesion_cuidado = SesionCuidado.objects.get(pk=sesion_cuidado_id)
    registro_cuidado = sesion_cuidado.registro_cuidado
    pregunta_cuidado = PreguntaCuidado.objects.filter(registro_cuidado=registro_cuidado).order_by('orden').first()
    return redirect('responder_pregunta', sesion_cuidado_id=sesion_cuidado.id, pregunta_cuidado_id=pregunta_cuidado.id)

def responder_pregunta(request, sesion_cuidado_id, pregunta_cuidado_id):
    sesion_cuidado = get_object_or_404(SesionCuidado, pk=sesion_cuidado_id)
    pregunta_actual = get_object_or_404(PreguntaCuidado, pk=pregunta_cuidado_id)

    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta:  # Basic validation
            with transaction.atomic():
                RespuestaCuidado.objects.create(
                    sesion_cuidado=sesion_cuidado,
                    pregunta_cuidado=pregunta_actual,
                    respuesta=respuesta,
                    usuario=request.user,
                )
            # Redirection logic
            siguiente_pregunta = PreguntaCuidado.objects.filter(
                registro_cuidado=sesion_cuidado.registro_cuidado, 
                orden__gt=pregunta_actual.orden
            ).order_by('orden').first()

            if siguiente_pregunta:
                return redirect('responder_pregunta', sesion_cuidado_id=sesion_cuidado.id, pregunta_cuidado_id=siguiente_pregunta.id)
            else:
                return redirect('resumen_sesion_cuidado', id_sesion=sesion_cuidado.id)
    
    return render(request, 'responder_pregunta.html', {'pregunta_cuidado': pregunta_actual})

def resumen_sesion_cuidado(request, id_sesion):
    sesion_cuidado = SesionCuidado.objects.get(pk=id_sesion)
    respuestas = RespuestaCuidado.objects.filter(sesion_cuidado=sesion_cuidado)

    return render(request, 'resumen_respuestas.html', {'respuestas': respuestas})
    
