from django.contrib import admin
from .models import Planta


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