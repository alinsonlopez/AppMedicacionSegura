from django import forms
from .models import Medicines


class MedicinesForm(forms.ModelForm):
    class Meta:
        model = Medicines
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
