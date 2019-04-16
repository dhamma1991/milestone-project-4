from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AccountCreationForm, AccountUpdateForm, ProfileUpdateForm

def register(request):
    """ 
    Enable creation of a new user account
    Render a blank form if a new request
    Render a partially filled in form if a subsequent request with failed validation
    Submit data to the database if data is valid
    """
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
    if request.method =='POST':
        # Post new data to the database
        # Define instance so the post knows which user to update
        account_form = AccountUpdateForm(request.POST, instance=request.user)
        # The file data coming in with the request will be the user-submitted image
        profile_form = ProfileUpdateForm(request.POST, 
                                        request.FILES, 
                                        instance=request.user.profile)
        
        # If both forms are valid
        if account_form.is_valid() and profile_form.is_valid():
            # Save both forms
            account_form.save()
            profile_form.save()
            
            # Feedback to the user
            messages.success(request, 'Your details have been successfully updated!')
            
            # Redirect back to the profile page
            # Any new details the user just submitted should be displayed
            return redirect('profile')
    else:
        account_form = AccountUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    # Pass the forms to the template using context
    context = {
        'account_form': account_form,
        'profile_form': profile_form
    }
    
    # Render the template with passed in context
    return render(request, 'accounts/profile.html', context)
    