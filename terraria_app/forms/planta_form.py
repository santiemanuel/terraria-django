from django import forms
from ..models import Planta

class PlantaForm(forms.ModelForm):
    fecha_adquisicion = forms.DateField(
        input_formats=['%Y-%m-%d', '%B %d, %Y'],
        widget=forms.DateInput(
            attrs={
                'type': 'text', 
                'class': 'ui calendar',
                'placeholder': 'Elige una fecha'
            }
        )
    )

    class Meta:
        model = Planta
        fields = ['nombre_comun', 'nombre_cientifico', 'fecha_adquisicion', 'imagen', 'ubicacion']
