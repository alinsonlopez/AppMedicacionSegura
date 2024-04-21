from django import forms
from .models import Medicines, Symptoms


class MedicinesForm(forms.ModelForm):
    class Meta:
        model = Medicines
        fields = '__all__'

class SymptomsForm(forms.ModelForm):
    class Meta:
        model = Symptoms
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
