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
    def test_can_get_tasks_page_with_user_logged_in(self):
        """
        With a user logged in, the app should be able to reach tasks.html
        """
        # Intialise Client
        c = Client()
        
        # Log in the user
        c.login(username='test_user', password='supersecretpa55')
        
        # Assert the tasks page can be reached
        page = c.get("/tasks/")
        self.assertEqual(page.status_code, 200)