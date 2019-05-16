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
    Test the functionality involved with the toggle_done_status view
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
                
        # Run the view, pass in required args
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of easy task is available for the test
        easy_task.refresh_from_db()
        
        """ Assert task can be been marked done """
        self.assertEqual(easy_task.done_status, True)
        
        """ Assert xp gained from easy task is 10 """
        self.assertEqual(request.user.profile.exp_points, 10)
        
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
            
        # Run the view, pass in required args
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of easy task is available for the test
        easy_task.refresh_from_db()
        
        """ Assert task can be been marked as done """
        self.assertEqual(easy_task.done_status, True)
        
        """ Assert xp gained from easy task is 10 """
        self.assertEqual(request.user.profile.exp_points, 10)
        
        # Run the view again to simulate task being marked as undone, pass in required args
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of easy task is available for the test
        easy_task.refresh_from_db()
        
        """ Assert task is now NOT done """
        self.assertEqual(easy_task.done_status, False)
        
        """ Assert user xp has gone back to 0 """
        self.assertEqual(request.user.profile.exp_points, 0)
        
    def test_user_who_exceeds_xp_threshold_levels_up_with_correct_xp(self):
        """
        Test that a user gains a level if they exceed their current xp threshold
        Also ensure that any 'leftover' gets set as their new xp amount
        """
        # Create an ambitious task
        amb_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task EA', task_difficulty = 'AM')
        
        # Grab the id and difficulty of the task
        task_id = amb_task.id
        task_difficulty = amb_task.task_difficulty
        
        # Make a request
        request = self.factory.post('/tasks/done/{}/{}'.format(task_id, task_difficulty))
        
        # Set the user
        request.user = self.user
        
        # Give the user some XP. The threshold for a level 1 user defaults to 100 so 
        # 90 xp should mean they need at least 10 to level up
        request.user.profile.exp_points = 90
        
        # Adding session
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        # Adding messages
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        
        # Run the view, pass in required args
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of the user is available for the test
        request.user.refresh_from_db()
        
        """ Assert that the user has 30 xp. 10 xp should of been used to get the user to their threshold of 100
            The remainder gets added to their new xp value """
        self.assertEqual(request.user.profile.exp_points, 30)
        
        """ Assert that the user is now level 2 """
        self.assertEqual(request.user.profile.level_rank, 2)
        
        """ Assert that the user has a new xp_threshold """
        self.assertEqual(request.user.profile.xp_threshold, 200)
        
    def test_user_who_is_above_level_1_can_lose_level_if_they_go_below_0_xp(self):
        """
        Test that a user loses a level if fall below 0 xp
        This would be the case if a user marks a task as undone and loses too much xp
        """
        # Create an ambitious task marked as done
        amb_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task EA', task_difficulty = 'AM', done_status = True)
        
        # Grab the id and difficulty of the task
        task_id = amb_task.id
        task_difficulty = amb_task.task_difficulty
        
        # Make a request
        request = self.factory.post('/tasks/done/{}/{}'.format(task_id, task_difficulty))
        
        # Set the user
        request.user = self.user
        
        # Set the user as level 2
        request.user.profile.level_rank = 2
        # Set the user's xp threshold to 200
        request.user.profile.xp_threshold = 200
        
        # Adding session
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        # Adding messages
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        
        # Run the view, pass in required args. This sets the task as undone
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of the user is available for the test
        request.user.refresh_from_db()
        
        """ Assert that the user has 60 xp. An ambitious task being marked as undone loses 40xp
            A level 2 user with 0 xp should therefore fall to level 1 with 60 xp (level 1 xp threshold should be 100)"""
        self.assertEqual(request.user.profile.exp_points, 60)
        
        """ Assert that the user is now level 1 """
        self.assertEqual(request.user.profile.level_rank, 1)
        
        """ Assert that the user has a new xp_threshold """
        self.assertEqual(request.user.profile.xp_threshold, 100)
        
    def test_user_who_levels_up_is_restored_to_100_hp(self):
        """
        Test that a user who gains a level is granted the full hitpoints value (100)
        """
        # Create an ambitious task
        amb_task = Task.objects.create(user_id = self.user.id, task_name = 'Test Task EA', task_difficulty = 'AM')
        
        # Grab the id and difficulty of the task
        task_id = amb_task.id
        task_difficulty = amb_task.task_difficulty
        
        # Make a request
        request = self.factory.post('/tasks/done/{}/{}'.format(task_id, task_difficulty))
        
        # Set the user
        request.user = self.user
        
        # Give the user some XP. The threshold for a level 1 user defaults to 100 so 
        # 90 xp should mean they need at least 10 to level up
        request.user.profile.exp_points = 90
        # Give the user less than 100 hp. This ensures that the hp being restored to 100 is obvious
        request.user.profile.hitpoints = 50
        
        # Adding session
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        # Adding messages
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        
        # Run the view, pass in required args
        response = toggle_done_status(request, task_id = task_id, task_difficulty = task_difficulty)
        
        # Ensure the updated instance of the user is available for the test
        request.user.refresh_from_db()
        
        """ First, assert that the user is now level 2 """
        self.assertEqual(request.user.profile.level_rank, 2)
        
        """ Assert that the user's hp is now 100 """
        self.assertEqual(request.user.profile.hitpoints, 100)
        
        