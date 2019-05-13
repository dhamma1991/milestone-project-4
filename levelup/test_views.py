# Import necessary modules so that tests can be conducted
from django.test import TestCase
from django.shortcuts import get_object_or_404
# Import models
from django.contrib.auth.models import User
from tasks.models import Task
# Client can be used to act as a dummy web browser, it also gives access to some useful methods, such as login()
from django.test import Client
        
class TestViews(TestCase):
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
        
    def test_can_get_tasks_page_with_user_logged_in(self):
        """
        With a user logged in, the app should be able to reach tasks.html
        """
        # Intialise Client
        c = Client()
        
        # Create a user
        User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        
        # Log in the user
        c.login(username='test_user', password='supersecretpa55')
        
        # Assert the tasks page can be reached
        page = c.get("/tasks/")
        self.assertEqual(page.status_code, 200)
        
    def test_can_get_profile_page_with_user_logged_in(self):
        """
        With a user logged in, the app should be able to reach tasks.html
        """
        # Intialise Client
        c = Client()
        
        # Create a user
        User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        
        # Log in the user
        c.login(username='test_user', password='supersecretpa55')
        
        # Assert the tasks page can be reached
        page = c.get("/profile/")
        self.assertEqual(page.status_code, 200)
        
    def test_easy_task_completion_gives_10_xp(self):
        """
        If a user marks an easy task as complete, their xp should increment by 10
        """
        # Intialise Client
        c = Client()
        
        # Create a user
        User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        
        # Log in the user
        c.login(username='test_user', password='supersecretpa55')
        
        # Create a task
        task = Task(task_name = "Test Task", task_difficulty = 'EA')
        
        page = c.get("/profile/")
        self.assertEqual(page.status_code, 200)

        
    
    # def test_get_edit_item_page(self):
    #     item = Item(name="Create a Test")
    #     item.save()

    #     page = self.client.get("/edit/{0}".format(item.id))
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "item_form.html")
    
    # def test_get_edit_page_for_item_that_does_not_exist(self):
    #     page = self.client.get("/edit/1")
    #     self.assertEqual(page.status_code, 404)
    
    # def test_post_create_an_item(self):
    #     response = self.client.post("/add", {"name": "Create a Test"})
    #     item = get_object_or_404(Item, pk=1)
    #     self.assertEqual(item.done, False)
    
    # def test_post_edit_an_item(self):
    #     item = Item(name="Create a Test")
    #     item.save()
    #     id = item.id

    #     response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
    #     item = get_object_or_404(Item, pk=id)

    #     self.assertEqual("A different name", item.name)
    
    # def test_toggle_status(self):
    #     item = Item(name="Create a Test")
    #     item.save()
    #     id = item.id

    #     response = self.client.post("/toggle/{0}".format(id))

    #     item = get_object_or_404(Item, pk=id)
    #     self.assertEqual(item.done, True)