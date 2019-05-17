# Import necessary modules so that tests can be conducted
import datetime
from datetime import timedelta
# Import Django components
from django.test import TestCase, RequestFactory
from django.shortcuts import get_object_or_404
from django.utils.timezone import make_aware
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.storage.fallback import FallbackStorage
# Import models
from django.contrib.auth.models import User
from tasks.models import Task
from stats.models import StatsModel
# Import views
from tasks.views import get_tasks
# Import Client
from django.test import Client
        
class TestGetTasks(TestCase):
    """
    Test the functionality involved with the get_tasks view
    """
    def setUp(self):
        """
        Create a user and a task
        """
        user1 = User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        task1 = Task.objects.create(task_name = 'Test Task 1', task_difficulty = 'ME', user = user1)
        
    def test_can_get_tasks_page_with_user_logged_in(self):
        """
        With a user logged in, the app should be able to reach tasks.html
        """
        # Log in the user
        self.client.login(username='test_user', password='supersecretpa55')
        
        # Go to the tasks page
        page = self.client.get("/tasks/")
        
        """ Assert that the page is found """
        self.assertEqual(page.status_code, 200)
        """ Assert that the template used is tasks.html """
        self.assertTemplateUsed('tasks.html')
        
class TestGetTasksRequestFactory(TestCase):
    """
    Test the functionality involved with the get_tasks view using RequestFactory
    """
    def setUp(self):
        """
        Basic set up
        Initialise RequestFactory
        """
        # Initialise RequestFactory
        self.factory = RequestFactory()
        # Create a user for ReqestFactory
        # Set their login as a date in the past
        self.user = User.objects.create_user(username = 'test_user_factory', 
            email = None,
            password = 'supersecretpa55', 
            # Setting the user's last login to be 7 days ago means that
            # every time the tests run, the get_tasks function will treat
            # the user as having logged in on a new day, triggering the task
            # reset functionality enabling it to be tested
            last_login = make_aware(datetime.datetime(d.year, d.month, d.day)))
        
    def test_user_with_an_uncompleted_easy_task_loses_10_hitpoints(self):
        # Create an easy task
        easy_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task EA', task_difficulty = 'EA')
        
        # Make a request
        request = self.factory.get('/tasks/')
        
        # Set the user
        request.user = self.user
        
        # Adding session
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        # Adding messages
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        
        # Run the view
        response = get_tasks(request)
        
        # Ensure the updated instance of user is available
        request.user.refresh_from_db()
        
        """ Assert that the user now has 90 hp """
        self.assertEqual(request.user.profile.hitpoints, 90)
        
        