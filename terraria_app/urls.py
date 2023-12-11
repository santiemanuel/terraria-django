from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path("plants/", views.plants, name="plants"),
    path("crear-pregunta/", views.crear_pregunta, name="crear_pregunta"),
    path("crear-planta/", views.crear_planta, name="crear_planta"),
    path('crear-registro-cuidado/', views.crear_registro_cuidado, name='crear_registro_cuidado'),
    path('plantas/registros/<int:planta_id>/', views.registros_planta_view, name='registros_planta'),
    path('registro-cuidado/<int:id>/', views.detalle_registro_cuidado_view, name='detalle_registro_cuidado'),
    path('registro-cuidado/<int:registro_cuidado_id>/crear-sesion/', views.crear_sesion_cuidado, name='crear_sesion_cuidado'),
    path('sesion-cuidado/<int:sesion_cuidado_id>/responder-preguntas/', views.responder_preguntas, name='responder_preguntas'),
    path('<sesion_cuidado_id>/responder-preguntas/', views.responder_preguntas, name='responder_preguntas'),
    path('sesion-cuidado/<int:sesion_cuidado_id>/responder-pregunta/<int:pregunta_cuidado_id>/', views.responder_pregunta, name='responder_pregunta'),
    path('sesion-cuidado/resumen/<int:id_sesion>/', views.resumen_sesion_cuidado, name='resumen_sesion_cuidado'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
