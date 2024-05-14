# memberships/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Progress, Class


class CustomUserCreationForm(UserCreationForm):
    health_details = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), required=False)
    address = forms.CharField(max_length=255, required=False)
    membership_start_date = forms.DateField(widget=forms.SelectDateWidget, required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'health_details', 'preferred_activities', 'address', 'membership_start_date')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'autofocus': True}))


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'description', 'start_time', 'end_time', 'instructor']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['activity', 'date', 'progress_detail']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'progress_detail': forms.Textarea(attrs={'rows': 4}),
        }