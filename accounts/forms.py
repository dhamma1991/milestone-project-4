from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# This class inherits from Django's built in user form
class AccountCreationForm(UserCreationForm):
    # This field is added to the form 
    # in addition to those already present in UserCreationForm
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']