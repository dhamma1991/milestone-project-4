from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.order_by('-created_date')
    context = {
        'task_list': task_list,
    }
    return render(request, 'tasks/tasks.html', context)
    
def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("The task you're trying to view does not exist")
    return render(request, 'tasks/task_detail.html', {'task': task})