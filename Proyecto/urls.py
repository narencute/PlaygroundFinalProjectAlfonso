"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from librosApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('librosApp/', include('librosApp.urls')),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('home/', views.home, name='home'),
    path('', views.home),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('<int:entrada_id>/', views.articulo_detallado, name='articulo_detallado'),
]
