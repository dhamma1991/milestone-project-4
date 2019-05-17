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
        # Go to the url
        page = self.client.get("/")
        
        """ Assert that the home page can be reached and that the template used is index.html """
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_get_signup_page(self):
        """
        Ensure that the signup page can be reached
        """
        # Go to the url
        page = self.client.get('/sign_up/')
        
        """ Assert that the signup page can be reached and that the template used is signup.html """
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/signup.html")
        
    def test_get_login_page(self):
        """
        Ensure that the login page can be reached
        """
        # Go to the url
        page = self.client.get('/login/')
        
        """ Assert that the login page can be reached and that the template used is login.html """
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/login.html")    
        
    def test_get_stats_page(self):
        """
        Ensure that the stats page can be reached
        """
        # Unless an instance of StatsModel exists, navigating to /stats/ throws a 404 error
        stats = StatsModel.objects.create(stats_name = 'Totals')
        
        # Go to the url
        page = self.client.get('/stats/')
        
        """ Assert that the stats page can be reached and that the template used is stats.html """
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "stats/stats.html")    
        
    def test_cannot_get_tasks_page_without_login(self):
        """
        Since there is no authenticated user in the class, trying to get to the tasks page should get a 302 code, as a redirect
        to login should occur
        """
        # Go to the url
        page = self.client.get("/tasks/")
        
        """ Assert that a redirection occurs """
        self.assertEqual(page.status_code, 302)
        
    def test_get_404_page_for_url_that_doesnt_exist(self):
        """
        Test that the 404 page appears when it should
        """
        # Go to a fake url
        page = self.client.get('/blahfooblahfooblah')
        
        """ Assert that a 404 error is thrown """
        self.assertEqual(page.status_code, 404)