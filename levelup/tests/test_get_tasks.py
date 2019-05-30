# Import necessary modules so that tests can be conducted
from datetime import timedelta
# Import Django components
from django.test import TestCase, RequestFactory
from django.utils import timezone
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
        self.user = User.objects.create_user(username = 'test_user_factory', 
            email = None,
            password = 'supersecretpa55')
        
        # Set the user's last login as a date in the past   
        # Setting the user's last login to be 2 days ago means that
        # every time the tests run, the get_tasks function will treat
        # the user as having logged in on a new day, triggering the task
        # reset functionality, enabling it to be tested
        self.user.profile.last_login = timezone.now() - timezone.timedelta(days = 2)
        
    def test_user_with_an_uncompleted_easy_task_loses_10_hitpoints(self):
        """
        Test that a user with an easy task not completed when a new day begins
        loses 10 hp
        """
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
        
    def test_user_with_an_uncompleted_medium_task_loses_20_hitpoints(self):
        """
        Test that a user with a medium task not completed when a new day begins
        loses 20 hp
        """
        # Create a medium task
        medium_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task ME', task_difficulty = 'ME')
        
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
        
        """ Assert that the user now has 80 hp """
        self.assertEqual(request.user.profile.hitpoints, 80)

    def test_user_with_an_uncompleted_hard_task_loses_30_hitpoints(self):
        """
        Test that a user with a hard task not completed when a new day begins
        loses 30 hp
        """
        # Create a hard task
        hard_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task HA', task_difficulty = 'HA')
        
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
        
        """ Assert that the user now has 70 hp """
        self.assertEqual(request.user.profile.hitpoints, 70)
        
    def test_user_with_an_uncompleted_ambitious_task_loses_40_hitpoints(self):
        """
        Test that a user with an ambitious task not completed when a new day begins
        loses 40 hp
        """
        # Create an ambitious task
        ambitious_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task AM', task_difficulty = 'AM')
        
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
        
        """ Assert that the user now has 60 hp """
        self.assertEqual(request.user.profile.hitpoints, 60)
        
    def test_user_with_an_uncompleted_easy_task_and_a_complete_medium_task_loses_10_hitpoints(self):
        """
        Test that a user with an easy task not completed when a new day begins
        loses 10 hp
        With a medium task complete, this medium task should not affect their hp
        """
        # Create an easy task
        easy_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task EA', task_difficulty = 'EA')
        # Create a medium task with a done_status of true
        medium_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task ME', task_difficulty = 'ME', done_status = True)
        
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
        
        # Ensure that the updated instance of medium_task is available
        medium_task.refresh_from_db()
        
        """ Assert that the user now has 90 hp """
        self.assertEqual(request.user.profile.hitpoints, 90)
        
        """ Assert that the done medium task is now not done since a new day has begun """
        self.assertEqual(medium_task.done_status, False)
        
    def test_user_who_goes_below_0_hp_loses_a_level_who_is_above_level_1(self):
        """
        Test that a level 2 or above user loses a level if they go below
        0 hp from uncompleted tasks
        """
        # Create an easy task
        easy_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task EA', task_difficulty = 'EA')
        # Create a medium task
        medium_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task ME', task_difficulty = 'ME')
        # With these two tasks, the user should lose 30 hp in total
        
        # Make a request
        request = self.factory.get('/tasks/')
        
        # Set the user
        request.user = self.user
        
        # Set the user to have 30 hp
        request.user.profile.hitpoints = 30
        
        # Set the user to be level 2
        request.user.profile.level_rank = 2
        
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
        
        """ Assert that the user now has 100 hp 
            When going to 0 hp, the user's hp is reset to 100
            If they are level 2 or above, they also lose a level """
        self.assertEqual(request.user.profile.hitpoints, 100)
        
        """ Assert that the formerly level 2 user is now level 1 """
        self.assertEqual(request.user.profile.level_rank, 1) 
        