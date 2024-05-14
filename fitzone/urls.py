# fitzone/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='memberships/login/', permanent=False)),
    path('admin/', admin.site.urls),
    path('memberships/', include('memberships.urls')),
]