from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.order_by('-created_date')
    template = loader.get_template('tasks/tasks.html')
    context = {
        'task_list': task_list,
    }
    return HttpResponse(template.render(context, request))
    
def detail(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)