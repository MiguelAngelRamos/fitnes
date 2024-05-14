#memberships/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Class

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Utiliza 'email' en lugar de 'username' para ordenar los usuarios
    ordering = ('email',)
    # Asegúrate de que el listado de campos en list_display no incluya 'username'
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')

    # Configuración de los formularios de edición y creación de usuarios
    fieldsets = (
        (None, {'fields': ('email', 'password', 'health_details', 'preferred_activities')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'health_details', 'preferred_activities', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Class)
