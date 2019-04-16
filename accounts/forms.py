from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class AccountCreationForm(UserCreationForm):
    """
    Allows user to create a new user account
    This class inherits from Django's built in user form
    """
    # This field is added to the form 
    # in addition to those already present in UserCreationForm
    email = forms.EmailField()
    
    class Meta:
        """
        Inherit the fields already present in Django's User model
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
   
class AccountUpdateForm(forms.ModelForm):
    """
    Allows users to update their user account details   
    """
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    """
    Allows users to update their user profile
    These are the fields that are added in addition to Django's standard User model
    """
    class Meta:
        model = Profile
        fields = ['image']