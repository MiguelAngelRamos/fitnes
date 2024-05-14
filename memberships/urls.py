# memberships/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, profile, class_list, class_create, class_update, class_delete, enroll_in_class, progress_list, progress_create, progress_update, progress_delete

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('classes/', class_list, name='class_list'),
    path('classes/create/', class_create, name='class_create'),
    path('classes/update/<int:pk>/', class_update, name='class_update'),
    path('classes/delete/<int:pk>/', class_delete, name='class_delete'),
    path('classes/enroll/<int:pk>/', enroll_in_class, name='enroll_in_class'),
    path('progress/', progress_list, name='progress_list'),
    path('progress/create/', progress_create, name='progress_create'),
    path('progress/update/<int:pk>/', progress_update, name='progress_update'),
    path('progress/delete/<int:pk>/', progress_delete, name='progress_delete'),
    # URLs para el restablecimiento de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]