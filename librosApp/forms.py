from django import forms
from .models import Comentario

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)
    
class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ('usuario', 'cuerpo', 'activo')
