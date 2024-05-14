# fitzone/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('memberships/', include('memberships.urls')),  # Incluir las URLs de la app memberships
]