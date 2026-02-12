
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("acercade/", views.acercade, name="acercaDe"),   
    path("contacto/", views.contacto, name="contacto"),    
    path("usuarios/", views.usuarios, name="usuarios"),
    path("logueado/", views.logueado, name="logueado"),    
    path("registro/", views.registro, name="registro"),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path("registro_viajes/", views.registro_viajes, name="registro_viajes"),
    
]
