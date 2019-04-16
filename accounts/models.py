from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # Create a one-to-one relationship with Django's User model
    # Ensure the profile is deleted if the user is deleted
    account = models.OneToOneField(User, on_delete = models.CASCADE)
    # Allow users to upload a profile image
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    
    
    def __str__(self):
        # Return how the class should be displayed
        return '%s Profile' % self.account.username
