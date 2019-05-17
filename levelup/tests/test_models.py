from django.test import TestCase
from tasks.models import Task
from accounts.models import Profile
from django.contrib.auth.models import User

class ModelTest(TestCase):
    def test_task_creation(self):
        """
        Test the Task model
        Test to ensure new instances of the Task model are created correctly
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
        """ Assert that the correct string representation of the object is returned """
        self.assertEqual(task.__str__(), task.task_name)
        
    def test_profile_creation(self):
        """
        Test the Profile model
        """
        # Create a user
        user = User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
    
        """ Assert that an instance of Profile was created along with user
            and that user.profile is an instance of Profile """
        self.assertTrue(isinstance(user.profile, Profile))
        
        """ Assert that the correct string representation of the object is returned """
        self.assertEqual(user.profile.__str__(), '%s Profile' % user.username)