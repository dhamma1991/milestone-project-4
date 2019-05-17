from django.test import TestCase
from django.contrib.auth.models import User

class LogInTest(TestCase):
    def setUp(self):
        """
        Create a user with some credentials
        """
        # Create credentials
        self.credentials = {
            'username': 'testuser',
            'password': 'secretpassword123'
        }
            
        # Create a user
        User.objects.create_user(**self.credentials)
        
    def test_login(self):
        """
        Check that a user can be logged in
        """
        # Send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        
        """ Assert the user is logged in """
        self.assertTrue(response.context['user'].is_active)