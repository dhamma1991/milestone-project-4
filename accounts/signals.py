# Signals could be specified directly in models.py
# However, doing it this way may prevent potential issues

"""
The idea behind this is that a profile should be created with each new user
"""

# Signal that gets fired after an object is saved
from django.db.models.signals import post_save
# The sender
from django.contrib.auth.models import User
# The receiver
from django.dispatch import receiver
# Import the necessary model
from .models import Profile

# When a user is saved, send a signal to this receiver
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    # If a user was created
    if created:
        # Create a profile object with the user equal to the instance of the
        # user that was created
        Profile.objects.create(account = instance)
        
# Save the profile every time the user object gets saved
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    # # # NOTE DIS MITE BE accounts NOT profile
    instance.profile.save()
