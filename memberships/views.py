#memberships/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Genera una contraseña temporal segura de 8 caracteres alfanuméricos.
            temp_password = get_random_string(8)
            user.set_password(temp_password)  # Establece la contraseña temporal.
            user.save()  # Guarda el usuario en la base de datos.
            # Envía un correo electrónico con la contraseña temporal.
            send_mail(
                'Tu Contraseña Temporal - FitZone',
                f'Hola {user.first_name}, aquí está tu contraseña temporal: {temp_password}\nPor favor cambia esta contraseña tras iniciar sesión por primera vez.',
                'mramoscli@outlook.com',  # Dirección de correo desde la que se envía el mensaje.
                [user.email],  # Lista de direcciones de correo a las que enviar el mensaje.
                fail_silently=False,
            )
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'memberships/register.html', {'form': form})
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Asegúrate de que 'login' es el nombre correcto para la URL de inicio de sesión
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'memberships/register.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'memberships/login.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')  # Asegúrate de que 'profile' es el nombre correcto para la URL de tu vista de perfil

@login_required
def profile(request):
    # Esta función asegura que solo los usuarios autenticados puedan ver la página del perfil
    # y pasa la instancia del usuario actual a la plantilla.
    return render(request, 'memberships/profile.html', {'user': request.user})

# Asegúrate de configurar las URLs para estas vistas en tu archivo urls.py
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')