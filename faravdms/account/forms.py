from dataclasses import field
import imp
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'