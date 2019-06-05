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
        
class TestLoginViews(TestCase):
    """
    Test the smaller views that require a login
    """
    def setUp(self):
        """
        Create a user
        """
        user = User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        
    def test_can_get_profile_page_with_user_logged_in(self):
        """
        With a user logged in, the app should be able to reach tasks.html
        """
        # Log in the user
        self.client.login(username='test_user', password='supersecretpa55')
        
        # Go to the profile page
        page = self.client.get("/profile/")
        
        """ Assert that the profile page is found """
        self.assertEqual(page.status_code, 200)
        """ Assert that profile.html is used as the template """
        self.assertTemplateUsed('profile.html')
        
    def test_newly_created_task_is_not_done(self):
        """
        A task that is created defaults to not done
        """
        # Log in the user
        self.client.login(username='test_user', password='supersecretpa55')
        
        # Create a task with a difficulty of easy
        task = Task(task_name = 'Test Task', task_difficulty = 'EA')
        
        """ Assert task.done_status is false """
        self.assertEqual(task.done_status, False)
        
    def test_user_can_reach_donate_page(self):
        """
        Test that the user is able to get to donate.html
        """
        # Log in the user
        self.client.login(username='test_user', password='supersecretpa55')
        
        # Go to donate.html
        page = self.client.get('/donate/')
        
        """ Assert that donate.html is reached """
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'accounts/donate.html')