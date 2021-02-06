from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = (
            'name',
            'description',
            'done',
            'date',
            'time',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date': forms.TextInput(attrs={'type': 'date','class': 'form-control'}),
            'time': forms.TextInput(attrs={'type': 'time','class': 'form-control'}),
        }

        labels = {
            'name': _('Nome'),
            'description': _('Descrição'),
            'done': _('Concluída'),
            'date': _('Data'),
            'time': _('Horário'),
        }
