# memberships/urls.py
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutViewcom
from django.urls import path, reverse_lazy
from .views import register, CustomLoginView, CustomLogoutView, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    # Asegúrate de usar reverse_lazy para definir la URL de redirección
    path('logout/', CustomLogoutView.as_view(), name="logout" ),
    # URLs para el restablecimiento de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
