from django import forms
from .models import Task, User
from django.forms.widgets import TextInput
class DateInput(TextInput):
    input_type = 'date'

class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Title',
    }))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Description',
    }))
    deadline = forms.DateTimeField(label='', 
    widget=forms.DateTimeInput(attrs={
        'class': 'form-control',
        'placeholder': 'Deadline',
    }))
    assigned_to = forms.ModelMultipleChoiceField( queryset=User.objects.filter(is_superuser=False, is_staff=False), label='', widget=forms.SelectMultiple(attrs={
        'class': 'form-control',
        'placeholder': 'Assigned to',
        'style': 'display:none;'
    }))
    assigned_input = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Assigned to',
    }))

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'assigned_to']
