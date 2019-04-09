from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=70)
    task_notes = models.TextField(max_length=400, blank=True)
    created_date = models.DateTimeField(editable=False, default=timezone.now())
    
    def __str__(self):
        return self.task_name