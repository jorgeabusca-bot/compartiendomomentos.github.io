Aquí tienes un ejemplo de un archivo `README.md` que documenta todas las correcciones y cambios realizados en tu proyecto Django para el manejo de usuarios:

```markdown
# Proyecto Django - Gestión de Usuarios

Este proyecto es una aplicación Django que permite el registro e inicio de sesión de usuarios utilizando un modelo de usuario personalizado. A continuación, se detallan las correcciones y configuraciones implementadas para asegurar el correcto funcionamiento del sistema de autenticación.

## Estructura del Proyecto

- `core/`: Aplicación principal que contiene la lógica del negocio.
- `core/models.py`: Definición del modelo de usuario.
- `core/views.py`: Lógica de las vistas para el registro e inicio de sesión.
- `projecto/settings.py`: Configuración del proyecto Django.

## Correcciones Realizadas

### 1. Modelo de Usuario Personalizado

Se creó un modelo de usuario personalizado en `core/models.py` que extiende `AbstractBaseUser` y utiliza un administrador de usuarios personalizado (`UsuarioManager`).

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, password=None, **extra_fields):
        if not usuario:
            raise ValueError('El nombre de usuario debe ser obligatorio')
        usuario = self.model(usuario=usuario, **extra_fields)
        usuario.set_password(password)  # Usa el método para establecer la contraseña
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    correo = models.EmailField(max_length=254)
    celular = models.CharField(max_length=20)
    usuario = models.CharField(max_length=100, unique=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'dni', 'correo', 'celular']   
    
    def __str__(self):
        return self.usuario 
```

### 2. Configuración del Proyecto

Se configuró el archivo `settings.py` para utilizar el modelo de usuario personalizado:

```python
AUTH_USER_MODEL = 'core.Usuario'  # Asegúrate de que este es el nombre correcto de tu modelo
```

### 3. Vista de Registro

Se corrigió la vista de registro para asegurar que la contraseña se establezca correctamente utilizando el método `set_password`. También se eliminó la autenticación inmediata después del registro.

```python
def registro(request):
    if request.method == "GET":
        return render(request, "core/registro.html")
    
    elif request.method == "POST":
        # Obtener datos del formulario
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        dni = request.POST.get("dni")
        correo = request.POST.get("correo")
        celular = request.POST.get("celular")
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")
        verificacion = request.POST.get("verificacion")
        
        # Verificación de contraseñas
        if password != verificacion:
            messages.error(request, "La contraseña y la verificación no coinciden.")
            return redirect("registro")
        
        # Verificación de existencia de nombre de usuario
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
            usuario=usuario
        )
        nuevo_usuario.set_password(password)  # Establecer la contraseña correctamente

        try:
            nuevo_usuario.save()
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect("usuarios")  # Redirigir a la página de inicio de sesión
        except Exception as e:
            messages.error(request, f"Error inesperado: {e}")
            return redirect("registro")
```

### 4. Vista de Inicio de Sesión

Se revisó la vista de inicio de sesión para autenticar correctamente a los usuarios utilizando el modelo personalizado.

```python
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
            return redirect("logueado")
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
            return render(request, "core/usuarios.html")
```

### 5. Migraciones

Asegúrate de ejecutar las migraciones después de realizar cambios en el modelo:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Prueba del Flujo Completo

1. **Registro**: Prueba registrar un nuevo usuario a través del formulario de registro.
2. **Inicio de sesión**: Después de registrar, intenta iniciar sesión con el nombre de usuario y la contraseña que acabas de registrar.

## Notas Finales

Si encuentras algún problema o error, asegúrate de revisar los mensajes de error y ajusta los métodos y configuraciones según sea necesario. Este proyecto está diseñado para ser una base sólida para la gestión de usuarios en una aplicación Django.

```

### Instrucciones para Usar el README

- Puedes copiar y pegar este contenido en un archivo llamado `README.md` en la raíz de tu proyecto.
- Asegúrate de que todos los nombres de archivos y rutas sean correctos según la estructura de tu proyecto.
- Personaliza cualquier sección según sea necesario para que se ajuste mejor a tus necesidades.

Si necesitas más ajustes o información adicional, no dudes en decírmelo.