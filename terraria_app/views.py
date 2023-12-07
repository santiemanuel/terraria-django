from django.shortcuts import render, redirect
from .models import Planta, RespuestaCuidado
from .forms.registro_form import RegistroCuidadoForm

def home(request):
    return render(request, "home.html")

def plants(request):
    plantas = Planta.objects.all() 
    return render(request, 'plantas.html', {'plantas': plantas})

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
                RespuestaCuidado.objects.create(
                    registro_cuidado=registro_cuidado,
                    pregunta=pregunta,
                    orden=orden
                )

            return redirect('alguna_url_despues_de_crear')  # Redirigir a donde sea necesario
    else:
        form = RegistroCuidadoForm()

    return render(request, 'crear_registro_cuidado.html', {'form': form})
