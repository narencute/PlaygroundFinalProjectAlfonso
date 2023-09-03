from django.contrib import admin
from librosApp.models import Entrada, Autor, Editorial, Libro, Mensaje, Comentario, Categoria

# Register your models here.
#admin.site.register(Entrada)
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Mensaje)

class EntradaAdmin(admin.ModelAdmin):
    fields = ('titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor', 'categorias', 'slug')
    
    prepopulated_fields = {'slug':('titulo',)}

admin.site.register(Categoria)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Comentario)
