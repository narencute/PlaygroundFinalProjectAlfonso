from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    fecha_publicacion = models.DateField()
    
    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.titulo
    
class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    imagen = models.URLField(max_length=1000)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField("Categoria")
    slug = models.SlugField(unique=True)
    #destacado = models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
        # Genera el slug automáticamente a partir del título
        self.slug = slugify(self.titulo)
        super(Entrada, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.titulo
    
class Mensaje(models.Model):
    email = models.EmailField(max_length=60)
    mensaje = models.TextField(max_length=500)
    
    def __str__(self):
        return self.email
    
class Comentario(models.Model):
    articulo = models.ForeignKey("Entrada", on_delete=models.CASCADE, related_name="comentario")
    usuario = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Comentario de {self.usuario}"
    
