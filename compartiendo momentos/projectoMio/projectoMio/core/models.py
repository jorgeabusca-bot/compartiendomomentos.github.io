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


# Create your models here.

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
