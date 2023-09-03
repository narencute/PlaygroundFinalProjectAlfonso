from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Libro, Autor, Editorial, Entrada, Mensaje, Comentario
from .forms import LibroForm, AutorForm, EditorialForm, BusquedaForm, ComentarioForm


# Create your views here.
def home(request):
    articulos = Entrada.objects.all()
    if request.method == "POST":
        email = request.POST["email"]
        mensaje = request.POST["mensaje"]
        obj = Mensaje(email=email, mensaje=mensaje)
        obj.save()
        respuesta = "Gracias por tu mensaje!"
        return render(request, "home.html",{"articulos":articulos, "respuesta":respuesta})
    return render(request, "home.html",{"articulos":articulos})

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, "iniciar_sesion.html", {'form': AuthenticationForm})
    else:
        name = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=name, password=password)
        if user is None:
            return render(request, "iniciar_sesion.html", {'form': AuthenticationForm, 'error': "Usuario o contraseña incorrectos"})
        else:
            login(request, user)
            return redirect("home")

def registro(request):
    if request.method == 'GET':
        return render(request, "registro.html", {'form': UserCreationForm})
    else:
        if request.POST["password1"] != request.POST["password2"]:
            return render(request, "registro.html", {'form': UserCreationForm, 'error': "Las contraseñas no coinciden."})
        else:
            name = request.POST["username"]
            password = request.POST["password1"]
            user = User.objects.create_user(username=name, password=password)
            user.save()
            return render(request, "registro.html", {'form': UserCreationForm, 'error': "Usuario Registrado correctamente"})
    
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

def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')

def articulo_detallado(request, entrada_id):
    articulo = Entrada.objects.get(id=entrada_id)
    
    comentarios = articulo.comentario.filter(activo=True)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_form = form.save(commit=False)
            nuevo_form.articulo = articulo
            nuevo_form.save()
            
    else:
        form = ComentarioForm
    
    return render(request, 'articulo.html', {'articulo':articulo, 'comentarios':comentarios, 'form':form})