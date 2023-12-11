from django import forms
from ..models import Pregunta
import json

class PreguntaForm(forms.ModelForm):
    opcion1 = forms.CharField(max_length=200, required=False)
    opcion2 = forms.CharField(max_length=200, required=False)
    opcion3 = forms.CharField(max_length=200, required=False)
    opcion4 = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Pregunta
        fields = ['texto', 'tipo', 'opcion1', 'opcion2', 'opcion3', 'opcion4']

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')

        if tipo == Pregunta.TIPO_OPCIONES:
            opciones = [cleaned_data.get(f'opcion{i}') for i in range(1, 5) if cleaned_data.get(f'opcion{i}').strip()]
            cleaned_data['opciones'] = json.dumps(opciones)
        
        return cleaned_data

    def save(self, commit=True):
        pregunta = super().save(commit=False)
        pregunta.opciones = self.cleaned_data['opciones']
        if commit:
            pregunta.save()
        return pregunta
