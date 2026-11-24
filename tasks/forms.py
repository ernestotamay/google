from django import forms
from .models import List, Task

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['list']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'detail', 'repeat', 'date', 'time', 'list']