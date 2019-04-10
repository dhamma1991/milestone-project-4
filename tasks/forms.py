from django import forms # Import the django forms library
from .models import Task # Import the post class you created in models.py

class AddTaskForm(forms.ModelForm): # Create a form for creating blog posts using django's form library
    class Meta:
        model = Task
        fields = ('task_name', 'task_notes') # You only want fields on your form that the user can actually edit