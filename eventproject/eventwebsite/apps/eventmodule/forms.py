# events/forms.py
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%Y-%m-%d', '%m/%d/%Y'])  # Specify input formats
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location','num_attendees']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput)