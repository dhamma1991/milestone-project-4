from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
# Subclass the generic class-based view CreateView within SignUp
class SignUp(generic.CreateView):
    # Use built in UserCreationForm
    form_class = UserCreationForm
    # Use reverse_lazy instead of reverse
    # because for all generic class-based views the urls do not load 
    # when the file is imported, this is solved by reverse_lazy
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
