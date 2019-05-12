# Import Django components
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# Import models
from tasks.models import Task
from .models import StatsModel

def get_stats(request):
    """
    Render stats.html. Pass through required values
    """
    # Count all tasks currently in the database
    all_tasks = Task.objects.all().count()
    # Count all the users
    all_users = User.objects.all().count()
    # Get the current total xp gained on the app
    total_xp = get_object_or_404(StatsModel, stats_name = 'Totals').total_xp_gain
    # Get the current total levels gained on the app
    total_levels = get_object_or_404(StatsModel, stats_name = 'Totals').total_levels_gain
    
    
    context = {
       'all_tasks': all_tasks, 
       'all_users': all_users,
       'total_xp': total_xp,
       'total_levels': total_levels
    }
    return render(request, 'stats/stats.html', context)
