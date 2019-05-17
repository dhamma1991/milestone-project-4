# Enable working with streams
import io
# Import Django components
# from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
# Enable support for image formats
from PIL import Image

class Profile(models.Model):
    # Create a one-to-one relationship with Django's User model
    # Ensure the profile is deleted if the user is deleted
    account = models.OneToOneField(User, on_delete = models.CASCADE)
    # Allow users to upload a profile image
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    # The users hitpoints, new users start with 100
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
    # A last login field is built into Django's User model. However, in my case I specifically only want the day, so I thought it easier to just add it here
    last_login = models.DateTimeField(default = timezone.now())
    # If the user has donated, this is set to true
    has_donated = models.BooleanField(default = False)
    
    
    
    
    def __str__(self):
        # Return how the class should be displayed
        return '%s Profile' % self.account.username
        
    # # Override the save method
    # def save(self, *args, **kwargs):
    #     # Run the save method of the parent class
    #     super().save(*args, **kwargs)
    #     # Open the image of the current instance
    #     img = Image.open(self.image.path)
        
    #     # If the image is larger than the site's required dimensions
    #     if img.height > 150 or img.width > 150:
    #         # Specify the values the image will be resized to
    #         output_size = (150, 150)
    #         # Resize the image, this will keep the image's proportions
    #         img.thumbnail(output_size)
    #         # Save
    #         img.save(self.image.path)
    
    def save(self, *args, **kwargs):
        """
        Overwrite the save method to resize a user uploaded image
        With thanks to caiolopes and this gist https://gist.github.com/caiolopes/a9f2bd942fa2d18412ac0d68a915eedf
        """
        super().save(*args, **kwargs)
    
        img_read = storage.open(self.image.name, 'r')
        img = Image.open(img_read)
    
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            in_mem_file = io.BytesIO()
            img.save(in_mem_file, format='JPEG')
            img_write = storage.open(self.image.name, 'w+')
            img_write.write(in_mem_file.getvalue())
            img_write.close()
    
        img_read.close()