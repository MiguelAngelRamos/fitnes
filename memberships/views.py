#memberships/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ClassForm, ProgressForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import Class, Progress

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            temp_password = get_random_string(8)
            user.set_password(temp_password)
            user.save()
            send_mail(
                'Tu Contraseña Temporal - FitZone',
                f'Hola {user.first_name}, aquí está tu contraseña temporal: {temp_password}\nPor favor cambia esta contraseña tras iniciar sesión por primera vez.',
                'mramoscli@outlook.com',
                [user.email],
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
        return reverse_lazy('class_list')  # Redirigir a la lista de clases después de iniciar sesión
    # def get_success_url(self):
    #     return reverse_lazy('profile')  # Asegúrate de que 'profile' es el nombre correcto para la URL de tu vista de perfil

@login_required
def profile(request):
    # Esta función asegura que solo los usuarios autenticados puedan ver la página del perfil
    # y pasa la instancia del usuario actual a la plantilla.
    return render(request, 'memberships/profile.html', {'user': request.user})

# Asegúrate de configurar las URLs para estas vistas en tu archivo urls.py
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
@login_required
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'memberships/class_list.html', {'classes': classes})

@login_required
def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'memberships/class_form.html', {'form': form})

@login_required
def class_update(request, pk):
    class_instance = Class.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_instance)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm(instance=class_instance)
    return render(request, 'memberships/class_form.html', {'form': form})

@login_required
def class_delete(request, pk):
    class_instance = Class.objects.get(pk=pk)
    if request.method == 'POST':
        class_instance.delete()
        return redirect('class_list')
    return render(request, 'memberships/class_confirm_delete.html', {'class_instance': class_instance})

@login_required
def enroll_in_class(request, pk):
    class_instance = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        class_instance.participants.add(request.user)
        return HttpResponseRedirect(reverse_lazy('class_list'))
    return render(request, 'memberships/class_enroll_confirm.html', {'class_instance': class_instance})

@login_required
def progress_list(request):
    progresses = Progress.objects.filter(user=request.user)
    return render(request, 'memberships/progress_list.html', {'progresses': progresses})

@login_required
def progress_create(request):
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = request.user
            progress.save()
            return redirect('progress_list')
    else:
        form = ProgressForm()
    return render(request, 'memberships/progress_form.html', {'form': form})

@login_required
def progress_update(request, pk):
    progress = get_object_or_404(Progress, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProgressForm(request.POST, instance=progress)
        if form.is_valid():
            form.save()
            return redirect('progress_list')
    else:
        form = ProgressForm(instance=progress)
    return render(request, 'memberships/progress_form.html', {'form': form})

@login_required
def progress_delete(request, pk):
    progress = get_object_or_404(Progress, pk=pk, user=request.user)
    if request.method == 'POST':
        progress.delete()
        return redirect('progress_list')
    return render(request, 'memberships/progress_confirm_delete.html', {'progress': progress})
