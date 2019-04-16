from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AccountCreationForm

def register(request):
    if request.method == 'POST':
        # Create an instance of UserCreationForm with user submitted data
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Create 'username' variable from username cleaned input
            username = form.cleaned_data.get('username')
            
            messages.success(request, 'Account created successfully! Please sign in.')
            
            return redirect('login')
    else:
        # Create a blank instance of the UserCreationForm called 'form'
        form = AccountCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
  
# Ensure a user is logged in to be able to view the profile page
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
    