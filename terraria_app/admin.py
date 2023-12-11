from django.contrib import admin
from .models.planta import Planta
from .models.pregunta import Pregunta


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'opciones', 'tipo')
    list_filter = ('texto', 'opciones', 'tipo')
    search_fields = ('texto', 'opciones')

    fieldsets = (
        (None, {
            'fields': ('texto', 'opciones', 'tipo')

        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('texto', 'opciones', 'tipo')}
        ),
    )

@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    list_display = ('nombre_comun', 'nombre_cientifico', 'fecha_adquisicion', 'imagen', 'ubicacion')
    list_filter = ('nombre_comun', 'nombre_cientifico', 'fecha_adquisicion', 'imagen', 'ubicacion')
    search_fields = ('nombre_comun', 'nombre_cientifico', 'fecha_adquisicion', 'imagen', 'ubicacion')

    fieldsets = (
        (None, {
            'fields': ('nombre_comun', 'nombre_cientifico', 'fecha_adquisicion', 'imagen', 'ubicacion')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombre_comun', 'nombre_cientifico', 'fecha_adquisicion', 'imagen', 'ubicacion')}
        ),
    )