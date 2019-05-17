from django.test import TestCase
from tasks.models import Task
from django.contrib.auth.models import User

class TaskTest(TestCase):
    """
    Test the Task model
    """
    def test_task_creation(self):
        """
        Test to ensure when a task is created it is an instance of the Task model
        """
        # Create a user
        user = User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        
        # Grab the user id
        user_id = user.id
        
        # Log in the user
        self.client.login(username='test_user', password='supersecretpa55')
        
        # Create a task, pass in the user_id as the task's user_id
        task = Task.objects.create(task_name = 'Test Task', task_difficulty = 'EA', user_id = user_id)
        
        """ Assert task is an instance of Task """
        self.assertTrue(isinstance(task, Task))