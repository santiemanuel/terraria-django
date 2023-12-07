from django.contrib import admin
from .models.planta import Planta
from .models.pregunta import Pregunta


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'opciones')
    list_filter = ('texto', 'opciones')
    search_fields = ('texto', 'opciones')

    fieldsets = (
        (None, {
            'fields': ('texto', 'opciones')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('texto', 'opciones')}
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