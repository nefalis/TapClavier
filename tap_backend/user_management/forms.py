from django import forms
from django.contrib.auth.models import User
from .models import SubProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class SubProfileForm(forms.ModelForm):
    class Meta:
        model = SubProfile
        fields = ['name']
