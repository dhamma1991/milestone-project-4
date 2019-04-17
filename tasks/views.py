from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import Task
from .forms import AddTaskForm

# Task Difficulty xp vars
xp_eas = 10
xp_med = 20
xp_har = 30
xp_amb = 40
    
# Filter goes here to filter by user
def get_tasks(request):
    task_list = Task.objects.order_by('-created_date').filter(user=request.user)
    context = {
        'task_list': task_list,
    }
    return render(request, 'tasks/tasks.html', context)
    
# User filter will need to go here for security
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def create_task(request):
    if request.method=="POST":
        # Construct the post form with user inputted data from the submitted form
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:get_tasks')
    else:
        form = AddTaskForm()
        
    return render(request, 'tasks/add_task_form.html', {'form': form})
    
def toggle_done_status(request, task_id):
    """
    Update the task status from done if it is undone and undone if it is done
    """
    task = get_object_or_404(Task, pk=task_id)
    task.done_status = not task.done_status
    task.save()
    
    user = request.user
    user.profile.exp_points += xp_eas
    user.profile.save()
    
    return redirect('tasks:get_tasks')
    
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('tasks:get_tasks')