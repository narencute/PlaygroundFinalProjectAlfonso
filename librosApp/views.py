from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Entrada, Mensaje, Comentario, Categoria
from .forms import BusquedaForm, ComentarioForm


# Create your views here.
def home(request):
    articulos = Entrada.objects.all()
    categorias = Categoria.objects.all()
    if request.method == "POST":
        email = request.POST["email"]
        mensaje = request.POST["mensaje"]
        obj = Mensaje(email=email, mensaje=mensaje)
        obj.save()
        respuesta = "Gracias por tu mensaje!"
        return render(request, "home.html",{"articulos":articulos, "categorias":categorias, "respuesta":respuesta})
    return render(request, "home.html",{"articulos":articulos, "categorias":categorias})

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
    
def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            articulos = Entrada.objects.filter(titulo__icontains=busqueda)
            return render(request, 'resultados_busqueda.html', {'articulos': articulos})
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