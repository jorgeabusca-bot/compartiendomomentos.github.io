from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from .models import Usuario  # Asegúrate de importar tu modelo Usuario

# Create your views here.


def index(request):
    return render(request, "core/index.html")

def acercade(request):
    return render(request, "core/acercaDe.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contacto(request):
    return render(request, "core/contacto.html")

def usuarios(request):
    if request.method == "GET":
        return render(request, "core/usuarios.html")
    elif request.method == "POST":
        username = request.POST.get("usuario")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect("logueado")# Redirige a la página de logueado
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
            return render(request, "core/usuarios.html")
        
def cerrar_sesion(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect( "index")
        

def registro(request):
    if request.method == "GET":
        return render(request, "core/registro.html")
    
    elif request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        dni = request.POST.get("dni")
        correo = request.POST.get("correo")
        celular = request.POST.get("celular")
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")
        verificacion = request.POST.get("verificacion")
        
        # Verifica que la contraseña y la verificación coincidan antes de crear el objeto
        if password != verificacion:
            messages.error(request, "La contraseña y la verificación no coinciden.")
            return redirect("registro")
        
        # Verifica si el nombre de usuario ya existe
        if Usuario.objects.filter(usuario=usuario).exists():
            messages.error(request,"El nombre de usuario ya está en uso. Por favor elige otro.")
            return render(request, "core/registro.html")
         # Crear el nuevo usuario
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            dni=dni,
            correo=correo,
            celular=celular,
            usuario=usuario,
        )
        nuevo_usuario.set_password(password),# Hash de la contraseña
        

        try:
            # Guardar el nuevo usuario en la base de datos
            nuevo_usuario.save()  # Esto asume que tu modelo Usuario tiene un método save()
            messages.error(request,"Usuario registrado exitosamente.")
            return redirect("usuarios")# Esto redirige a la página de inicio de sesión

        except ValueError as e:
            messages.error(request,f"Error en el registro: {e}")
            return redirect("registro")
        except Exception as e:
            messages.error(request,f"Error inesperado: {e}")
            return redirect("registro")                 

def registro_viajes(request):
    return render(request, "core/registro_viajes.html")


def logueado(request):
    return render(request, "core/logueado.html",  {'user': request.user})