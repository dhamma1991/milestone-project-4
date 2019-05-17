from django.test import TestCase
# Import forms to test
from tasks.forms import AddTaskForm
from accounts.forms import AccountCreationForm

"""
These tests are aimed mostly at built-in Django components, so should be expected to pass without difficulty
"""

class TestAddTaskForm(TestCase):
    def test_can_create_an_task_with_just_a_name_and_difficulty(self):
        """
        Test that a user can create a task with just a task name and difficulty set
        Task notes are also part of the model, but this is an optional field
        """
        form = AddTaskForm({
            'task_name': 'Do Tests', 
            'task_difficulty': 'EA'
        })
        
        """ Assert that form.is_valid() is true """
        self.assertTrue(form.is_valid())
        
    def test_add_task_form_is_invalid_with_missing_name(self):
        """
        Test that the add task form is invalid if the required task_name field is missing
        """
        form = AddTaskForm({'task_name': ''})
        
        """ The form can not be valid because the value is missing so should assert false """
        self.assertFalse(form.is_valid())
        
class TestCreateAccountForm(TestCase):
    def test_can_create_user(self):
        """
        Test that users can be created using the create account form
        """
        form = AccountCreationForm({
            'username': 'TestUser', 
            'email': 'test@testing.com', 
            'password1': 'testpass98765',
            'password2': 'testpass98765'
        })
        
        """ Assert the form is valid """
        self.assertTrue(form.is_valid())
        
    def test_password1_and_password2_match(self):
        """
        Test that Django takes care of ensuring that matching passwords are submitted when an account is created
        """
        form = AccountCreationForm({
            'username': 'TestUser', 
            'email': 'test@testing.com', 
            'password1': 'iamnotamatchingpassword123',
            'password2': 'testpass98765'   
        })
        
        """ The two passwords above do not match, so this should assert false """
        self.assertFalse(form.is_valid())