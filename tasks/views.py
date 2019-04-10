from django.http import Http404
from django.shortcuts import render, get_object_or_404
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
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})