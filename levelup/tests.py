from django.test import TestCase

class TestDjango(TestCase):
    
    """ Ensure the test framework is functioning """
    def test_sanity_equal(self):
        self.assertEqual(1,1)
        
    """ This test should fail """
    # def test_sanity_equal_two(self):
    #     self.assertEqual(1,0)
