from django.urls import path
from . import views

urlpatterns = [
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_editorial/', views.agregar_editorial, name='agregar_editorial'),
    path('buscar/', views.buscar, name='buscar'),
]