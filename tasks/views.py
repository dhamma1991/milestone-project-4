from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import AddTaskForm

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def tasks(request):
    task_list = Task.objects.order_by('-created_date')
    context = {
        'task_list': task_list,
    }
    return render(request, 'tasks/tasks.html', context)
    
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})
    
# def create_or_edit_task(request, pk):
#     """
#     Create a view that allows users to create or edit a task
#     Depending if the Post ID is null or not
#     """
    
#     # get_object_or_404 either gets the object or returns a 404
#     task = get_object_or_404(Task, pk=pk)
#     # If the form is posted
#     if request.method == "POST":
#         # Render the blogpostform
#         form = AddTaskForm(request.POST)
#         if form.is_valid():
#             task = form.save()
#             # Redirect to the post detail using the post id
#             return redirect(index)
            
#     else:
#         form = AddTaskForm(instance=task)
    
#     return render(request, "add_task_form.html", {'form': form})

def create_task(request):
    if request.method=="POST":
        # Construct the post form with user inputted data from the submitted form
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('tasks:index')
    else:
        form = AddTaskForm()
        
    return render(request, 'tasks/add_task_form.html', {'form': form})
    
def toggle_done_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done_status = not task.done_status
    task.save()
    return redirect('tasks:index')