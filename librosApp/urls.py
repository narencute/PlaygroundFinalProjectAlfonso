from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('buscar/', views.buscar, name='buscar'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('<int:entrada_id>/', views.articulo_detallado, name='articulo_detallado'),
]