from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('usuario', 'correo', 'nombre', 'apellido')  # Campos que deseas mostrar
    list_filter = ('nombre', 'apellido')  # Campos por los que puedes filtrar
    ordering = ('usuario',)
    search_fields = ('usuario', 'correo')  # Campos por los que puedes buscar
    fieldsets = (
        (None, {'fields': ('usuario', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'dni', 'correo', 'celular')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('usuario', 'password1', 'password2', 'nombre', 'apellido', 'dni', 'correo', 'celular')}
        ),
    )
    # Si no tienes grupos y permisos, puedes omitir estos campos
    filter_horizontal = ()  # Si no usas grupos y permisos
    ordering = ('usuario',)

# Registra tu modelo con la clase de administración personalizada
admin.site.register(Usuario, CustomUserAdmin)
