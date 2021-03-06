from django.contrib import admin
from .models import Task

# Register the admin class with the model
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Display the created date in the admin panel as read only
    readonly_fields = ('created_date',)