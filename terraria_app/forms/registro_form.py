from django import forms
from ..models import RegistroCuidado, Planta, Pregunta

class RegistroCuidadoForm(forms.ModelForm):
    planta = forms.ModelChoiceField(queryset=Planta.objects.all(), required=True, widget=forms.Select(attrs={'class': 'ui dropdown'}))
    preguntas = forms.ModelMultipleChoiceField(queryset=Pregunta.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'ui fluid dropdown'}))

    class Meta:
        model = RegistroCuidado
        fields = ['planta', 'preguntas']
