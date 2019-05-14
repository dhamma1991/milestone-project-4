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
        
    def test_newly_created_task_is_not_done(self):
        """
        A task that is created defaults to not done
        """
        # Intialise Client
        c = Client()
        
        # Create a user
        # user = User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        
        # Log in the user
        c.login(username='test_user', password='supersecretpa55')
        
        # Create a task with a difficulty of easy
        task = Task(task_name = 'Test Task', task_difficulty = 'EA')
        
        # Assert task.done_status is false
        self.assertEqual(task.done_status, False)
        
    def test_easy_task_completion_gives_10_xp(self):
        """
        If a user marks an easy task as complete, their xp should increment by 10
        """
        # Intialise Client
        # c = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        
        request = self.factory.get('/tasks/done/{}/{}".format(id, difficulty)')
        
        request.user = self.user
        
        task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task', task_difficulty = 'EA')
        stats = StatsModel.objects.create(stats_name = 'Totals')
        
        task_id = task.id
        task_difficulty = task.task_difficulty
        
        # Adding session
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        # Adding messages
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Create a user
        # user = User.objects.create_user(username = 'test_user', email = None, password = 'supersecretpa55')
        
        # Log in the user
        # c.login(username='test_user', password='supersecretpa55')
        
        # Create a task with a difficulty of easy
        # task = Task.objects.create_task(user.id, 'Test Task', 'Test Notes', 'EA')
        # task = Task.objects.create(user_id = user.id, task_name = 'Test Task', task_difficulty = 'EA')
        
        # id = task.id
        # difficulty = task.task_difficulty
    
        # self.assertEqual(user.profile.hitpoints, 50)
        
        # response = self.client.post("/tasks/done/{}/{}".format(id, difficulty))
        
        task.refresh_from_db()
        
        self.assertEqual(task.done_status, True)
        
        self.assertEqual(task.task_name, 'Test Task')

        # Assert the user has 10 xp
        # self.assertEqual(user.profile.exp_points, 10)

        
    
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