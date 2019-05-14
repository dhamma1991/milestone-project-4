# Import necessary modules so that tests can be conducted
from django.test import TestCase, RequestFactory
from django.shortcuts import get_object_or_404
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.storage.fallback import FallbackStorage
# Import models
from django.contrib.auth.models import User
from tasks.models import Task
from stats.models import StatsModel
# Import views
from tasks.views import toggle_done_status
# Client can be used to act as a dummy web browser, it also gives access to some useful methods, such as login()
from django.test import Client
        
class TestToggleDoneStatus(TestCase):
    """
    Test the functionality involved with the toggle_done_status views
    """
    def setUp(self):
        """
        Basic set up
        Initialise RequestFactory
        Create required instances
        Add session and middleware
        """
        # Initialise RequestFactory
        self.factory = RequestFactory()
        # Create a user for ReqestFactory
        self.user = User.objects.create_user(username = 'test_user_factory', email = None, password = 'supersecretpa55')
        
        # Create task instances
        medium_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task ME', task_difficulty = 'ME')
        hard_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task HA', task_difficulty = 'HA')
        ambitious_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task AM', task_difficulty = 'AM')
        
        # Create a stats instance, required as stats is referenced within toggle_done_status
        stats = StatsModel.objects.create(stats_name = 'Totals')
        
    def test_toggle_done_status_should_mark_a_task_as_true(self):
        """
        If a user marks an easy task as complete, their xp should increment by 10
        """
        # Create an easy task
        easy_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task EA', task_difficulty = 'EA')
        
        # Grab the id and difficulty of the task
        task_id = easy_task.id
        task_difficulty = easy_task.task_difficulty
        
        # Make a request
        request = self.factory.post('/tasks/done/{}/{}'.format(task_id, task_difficulty))
        
        # Set the user
        request.user = self.user
        
        # Adding session
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        # Adding messages
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        
        # Run the view, pass in required args
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of task is available for the test
        easy_task.refresh_from_db()
        
        # Assert the task is now done
        self.assertEqual(easy_task.done_status, True)
        
        # self.assertEqual(response.status_code, 301)

        # Assert the user has 10 xp
        # self.assertEqual(user.profile.exp_points, 10)