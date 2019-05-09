# Import Django components
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Import forms
from .forms import AccountCreationForm, AccountUpdateForm, ProfileUpdateForm

# Required for Stripe integration
import stripe

""" The register view """
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
  
""" The profile view """
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
         
        # If the account or profile forms are not valid    
        elif not account_form.is_valid() or profile_form.is_valid():
            # This is required in case the user tries to change their username to an already existing username on the db
            # The validation kicks in and prevents the change, but for some reason request.user still changes to the failed username
            # This means that the user sees the failed username on both the profile page, and also in the top right navigation
            # Not sure why this happens but the below line fixes it.
            request.user.refresh_from_db()
            
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
    
""" The donate view """    
@login_required
def donate(request):
    """
    Render the donation page and pass along the key required by Stripe
    """
    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY
    }
    
    return render(request, 'accounts/donate.html', context)
    
""" The charge view """    
def charge(request):
    """
    Make a 'charge' to the user and render charge.html
    """
    # Get the stripe API key
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    # If the user makes a post
    if request.method == 'POST':
        # Make a charge, pass in charge args
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Donate',
            source=request.POST['stripeToken']
        )
        
        # Get the current user
        user = request.user.profile
        
        # Set that the user has donated
        user.has_donated = True
        
        # Save changes to the model
        user.save()
        
        # Go to charge.html
        return render(request, 'charge.html')
    