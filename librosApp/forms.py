from django import forms
from .models import Libro, Autor, Editorial

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'genero', 'fecha_publicacion')
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellido', 'nacionalidad')

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ('nombre', 'pais')

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)