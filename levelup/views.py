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
    context = {
        'title': "LEVELUP | Productivity Reinvented"
    }
    
    return render(request, 'index.html', context)
""" /1. The index view """

""" 2. The donate view """
def donate(request):
    """
    Render the donation page and pass along the key required by Stripe
    """
    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'donate.html', context)
""" /2. The donate view """

""" 3. The charge view """    
def charge(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Donate',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')
""" /3. The charge view """    