from django.db import models
from django.contrib.auth.models import User

# class TaskManager(models.Manager):
#     """
#     Overwrite the model manager as recommended in the Django docs
#     Allows instantiation of the Task class
#     This is used for testing
#     """
#     def create_task(self, user_id, task_name, task_notes, task_difficulty):
#         task = self.create(user_id = user_id,
#             task_name = task_name,
#             task_notes = task_notes, 
#             task_difficulty = task_difficulty)
#         return task

class Task(models.Model):
    easy = 'EA'
    medium = 'ME'
    hard = 'HA'
    ambitious = 'AM'
    task_difficulty_choices = (
        (easy, 'Easy'),
        (medium, 'Medium'),
        (hard, 'Hard'),
        (ambitious, 'Ambitious')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    task_name = models.CharField(max_length=70)
    task_notes = models.TextField(max_length=400, blank=True)
    done_status = models.BooleanField(default=False)
    task_difficulty = models.CharField(max_length=2, choices=task_difficulty_choices, default=easy)
    created_date = models.DateTimeField(editable=False, blank=True, auto_now_add=True)
    
    # objects = TaskManager()
    
    def __str__(self):
        return self.task_name