from django import forms # Import the django forms library
from .models import Task # Import the post class you created in models.py

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_name', 'task_notes', 'task_difficulty')