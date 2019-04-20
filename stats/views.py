from django.shortcuts import render
from django.contrib.auth.models import User
from tasks.models import Task

def get_stats(request):
    """
    Render stats.html. Pass through required values
    """
    # Count all tasks currently in the database
    all_tasks = Task.objects.all().count()
    # Count all the users
    all_users = User.objects.all().count()
    
    context = {
       'all_tasks': all_tasks, 
       'all_users': all_users,
    }
    return render(request, 'stats/stats.html', context)
