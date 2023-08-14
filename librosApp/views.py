from django.shortcuts import render, redirect
from .models import Libro, Autor, Editorial
from .forms import LibroForm, AutorForm, EditorialForm, BusquedaForm

# Create your views here.
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_libro')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_autor')
    else:
        form = AutorForm()
    return render(request, 'agregar_autor.html', {'form': form})

def agregar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_editorial')
    else:
        form = EditorialForm()
    return render(request, 'agregar_editorial.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            libros = Libro.objects.filter(titulo__icontains=busqueda)
            return render(request, 'resultados_busqueda.html', {'libros': libros})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})