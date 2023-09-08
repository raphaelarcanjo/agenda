from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = ('name', 'description', 'done', 'date', 'time')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TextInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

        labels = {
            'name': _('Nome'),
            'description': _('Descrição'),
            'done': _('Concluída'),
            'date': _('Data'),
            'time': _('Horário'),
        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Obrigatório. Forneça um endereço de e-mail válido.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
