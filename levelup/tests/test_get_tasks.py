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