from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    """
    Render index.html
    """
    return render(request, 'index.html')
    
def donate(request):
    """
    Render the donation page and pass along the key required by Stripe
    """
    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'donate.html', context)