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
        
    def test_toggle_done_status_on_easy_task_marks_task_as_done_if_not_done_and_gives_10_xp(self):
        """
        Test the functionality involving toggle_done_status
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
                
        """ Assert task can be been marked done """
        # Run the view, pass in required args
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of easy task is available for the test
        easy_task.refresh_from_db()
        
        self.assertEqual(easy_task.done_status, True)
        
        """ Assert xp gained from easy task is 10 """
        self.assertEqual(request.user.profile.exp_points, 10)
        
        """ Assert task being marked as undone affects task.done_status and make user lose xp"""
        # Run the view again to simulate task being marked as undone, pass in required args
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of easy task is available for the test
        easy_task.refresh_from_db()
        
        # Assert the task is now NOT done
        self.assertEqual(easy_task.done_status, False)
        
        # Asset user xp has gone back to 0
        self.assertEqual(request.user.profile.exp_points, 0)
        
    def test_toggle_done_status_on_easy_task_marks_task_as_not_done_if_done_and_minuses_10_xp(self):
        """
        Test the functionality involving toggle_done_status
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
                
        """ Assert task can be been marked done """
        # Run the view, pass in required args
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of easy task is available for the test
        easy_task.refresh_from_db()
        
        self.assertEqual(easy_task.done_status, True)
        
        """ Assert xp gained from easy task is 10 """
        self.assertEqual(request.user.profile.exp_points, 10)