# Import necessary modules for testing
import os
from django.test import TestCase
from django.conf import settings

class TestDjango(TestCase):
    """ Ensure the test framework is functioning """
    def test_sanity_equal(self):
        self.assertEqual(1,1)
        
    """ This test should fail """
    # def test_sanity_equal_two(self):
    #     self.assertEqual(1,0)
    
class TestSettings(TestCase):
    """
    Test to ensure custom elements of settings.py are working as intended
    """
    def test_travis_build_is_correct(self):
        """
        Test to ensure that Django get's a Travis-specific secret key only on Travis
        """
        if os.environ.get('TRAVIS_BUILD'):
            self.assertEqual(settings.SECRET_KEY, 'wt5xd3fx+bgh+vo^hj!%l&-nag7ginpz7e@6t)gcf#(_@0ecjk')
        else:
            self.assertEqual(settings.SECRET_KEY, os.environ.get('SECRET_KEY'))
        
        
