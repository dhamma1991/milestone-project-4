# Import Django components
from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

"""
This file contains views that are related to the smaller elements of functionality within the project 
that do not justify their own Django app
"""

""" 1. The index view """
def index(request):
    """
    Render index.html
    """
    return render(request, 'index.html')

""" 2. The get started (about) view """
def get_started(request):
    """
    Render about.html
    """
    return render(request, 'about.html')