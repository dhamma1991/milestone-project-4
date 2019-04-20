from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

def index(request):
    """
    Render index.html
    """
    return render(request, 'index.html')