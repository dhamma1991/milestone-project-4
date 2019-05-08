from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect # Import necessary Django components

import stripe # Required for Stripe integration

"""
This file contains views that are related to the smaller elements of functionality within the project that do not justify their own Django app
Contained here are:
1. The index view
2. The donate view
3. The charge view 
"""

""" 1. The index view """
def index(request):
    """
    Render index.html
    """
    return render(request, 'index.html')

""" 2. The get started (help) view """
def get_started(request):
    """
    Render help.html
    """
    return render(request, 'help.html')

""" 3. The donate view """
def donate(request):
    """
    Render the donation page and pass along the key required by Stripe
    """
    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY
    }
    
    return render(request, 'donate.html', context)

""" 4. The charge view """    
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
        
        # Go to charge.html
        return render(request, 'charge.html')