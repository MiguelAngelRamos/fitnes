# memberships/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
#membership/forms.py
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    health_details = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'health_details', 'preferred_activities')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'autofocus': True}))
