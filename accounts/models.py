from datetime import date
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # Create a one-to-one relationship with Django's User model
    # Ensure the profile is deleted if the user is deleted
    account = models.OneToOneField(User, on_delete = models.CASCADE)
    # Allow users to upload a profile image
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    hitpoints = models.IntegerField(default = 100)
    # Users start off with 0 experience points
    exp_points = models.IntegerField(default = 0)
    # Users start off as level 1
    level_rank = models.IntegerField(default = 1)
    # The default experience points threshold to reach the next 
    # level is 100 (to reach level 2)
    xp_threshold = models.IntegerField(default = 100)
    # The user's last login is used to determine when task.done_status is refreshed
    # Default is when the user is created
    last_login = models.DateTimeField(default = date.today)
    
    
    
    
    def __str__(self):
        # Return how the class should be displayed
        return '%s Profile' % self.account.username
        
    
    # Override the save method
    def save(self, *args, **kwargs):
        # Run the save method of the parent class
        super().save(*args, **kwargs)

        # Open the image of the current instance
        img = Image.open(self.image.path)
        
        # If the image is larger than the site's required dimensions
        if img.height > 150 or img.width > 150:
            # Specify the values the image will be resized to
            output_size = (150, 150)
            # Resize the image, this will keep the image's proportions
            img.thumbnail(output_size)
            # Save
            img.save(self.image.path)