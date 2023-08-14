from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=20)

class Editorial(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=20)

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    fecha_publicacion = models.DateField()