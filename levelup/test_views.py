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
        
class TestViews(TestCase):
    """
    Test the smaller views that do not require a login
    """
    def test_get_home_page(self):
        """
        Simple url test, ensure that the home page can be reached
        """
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_cannot_get_tasks_page_without_login(self):
        """
        Since there is no authenticated user in the class yet, trying to get to the tasks page should get a 302 error, as a redirect
        to login should occur
        """
        page = self.client.get("/tasks/")
        self.assertEqual(page.status_code, 302)