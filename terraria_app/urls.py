from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path("plants/", views.plants, name="plants"),
    path('crear-registro-cuidado/', views.crear_registro_cuidado, name='crear_registro_cuidado'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
