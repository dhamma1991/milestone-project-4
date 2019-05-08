import datetime
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.timezone import make_aware
from accounts.models import Profile
from .models import Task
from .forms import AddTaskForm
    
@login_required
def get_tasks(request):
    # Get the list of tasks for the current logged in user
    task_list = Task.objects.order_by('-created_date').filter(user=request.user)
    
    # Get the current user
    user = request.user.profile
    
    # Grab the timestamp for the current request and make it into a format acceptable to the
    # last_login field
    # Only grab the current day
    # # # # # # # # IMPORTANT!!!!! Whilst testing, just set the 'day' argument in the replace function to the next day to simulate a day having passed
    current_login = make_aware(datetime.datetime.now()).replace(
        hour=0, minute=0, second=0, microsecond=0)
    
    # If the user gets tasks on a new day
    if current_login > user.last_login:
        # Initialize hitpoints_lost
        # This is to feedback to the user should they have lost hitpoints
        hitpoints_lost = 0
        # Initialise tasks_not_done
        # This is to feedback to the user the number of tasks they didn't complete
        # As well as the sum of any hitpoints lost
        tasks_not_done = 0
        # Initialise user_lost_level
        # This is used to check whether to feedback to the user that they have lost a level
        user_lost_level = False
        # Initialise user_is_level_one
        # This helps determine the mesage to shaw a user who is level 1 but loses all their hitpoints
        # Users cannot become level 0 or negative levels
        user_is_level_one = False
        
        # Go through each task
        for task in task_list:
            # And check if the task is not done
            # Check the task's difficulty and apply hp loss based on the task's difficulty
            # Harder tasks lose more hp when not done (to balance them giving more xp when done)
            if not task.done_status:
                # If a task is not done, increment tasks_not_done by 1
                tasks_not_done += 1
                if task.task_difficulty == 'EA':
                    user.hitpoints -= 10
                    hitpoints_lost += 10
                elif task.task_difficulty == 'ME':
                    user.hitpoints -=20
                    hitpoints_lost += 20
                elif task.task_difficulty == 'HA':
                    user.hitpoints -=30
                    hitpoints_lost += 30
                elif task.task_difficulty == 'AM':
                    user.hitpoints -=40
                    hitpoints_lost += 40
            
            # Then reset the done_status of each task to false since a new day has started
            task.done_status = False
            
            # Save any changes to task model
            task.save()
        
            # If the user has lost all their hitpoints
            if user.hitpoints <= 0:
                # Users who are level 1 when they lose all their hitpoints can not go below level 1
                if not user.level_rank == 1:
                    user_lost_level = True
                    # Reduce the user's level
                    user.level_rank -=1
                    # And set the new xp_threshold
                    user.xp_threshold -= 100
                else:
                    user_is_level_one = True
                # Reset the user's hitpoints
                user.hitpoints = 100
                # Reset the user xp
                user.exp_points = 0

        # If the tasks_not_done var has remained zero (all tasks completed)
        if not tasks_not_done:     
            messages.info(request, "A new day has begun! You managed to complete all your tasks yesterday. Great work!")
        else:
            # Inform the user that some tasks were not completed
            messages.info(request, "Looks like you didn't fully complete you tasks yesterday!")
            # If a user higher than level 1 loses a level
            if user_lost_level:
                messages.info(request, "You lost a level! Your xp will reset to 0.")
            # Else if a level 1 user 'loses' a level
            elif user_is_level_one:
                messages.info(request, "Don't worry, users who are level 1 cannot lose levels. Maybe you need to make your tasks easier in order to level up?")
            # If a user didn't lose a level but still lost hitpoints
            # Inform them of the amount of hitpoint loss
            else:
                messages.info(request, "Total hitpoints lost: {}".format(hitpoints_lost))
                
            # Inform users of the number of tasks they didn't complete
            messages.info(request, "Tasks not completed: {}".format(tasks_not_done))
        
        # Update user's last login to reflect the current day
        # The changes that occur above will occur again when another day has passed
        user.last_login = current_login
        
        # Finally, save any changes to user model
        user.save()            
        
    context = {
        'task_list': task_list,
        'current_login': current_login,
        # 'my_message': my_message,
        'last_login': user.last_login
    }
    
    return render(request, 'tasks/tasks.html', context)
    
@login_required
def detail(request, task_id):

    task = get_object_or_404(Task, pk=task_id)
    
    # Ensure only the user who created the task is able to view the task's detail
    if not request.user == task.user:
        # Return a 404 page
        return render(request, '404.html')
    
    # If the user trying to access the task's detail is indeed the user who created the task,
    # show them the page
    else:
        return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
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

@login_required    
def toggle_done_status(request, task_id, task_difficulty):
    """
    Update the task status from done if it is undone and undone if it is done
    Apply any xp and level gains/losses
    Feedback to the user the actions that are taken
    """
    
    task = get_object_or_404(Task, pk=task_id)
    
    # Ensure only the user who created the task is able to mark the task as done
    if not request.user == task.user:
        # Return a 404 page
        return render(request, '404.html')
    
    # If the user trying to mark the task as done is indeed the user who created the task,
    # allow them to carry out the action
    else:
        task.done_status = not task.done_status
        task.save()
        
        # Task Difficulty xp amounts
        # This gets passed through from the template when the user
        
        # Set the base xp amount
        # Using a base amount allows multipliers to be applied to higher difficulties
        # Makes this easier to change if I ever decide to change how xp rewards are calculated
        base_xp = 10
        
        # Set base xp_threshold increment
        # Again, if this ever needs changing
        base_xp_threshold = 100
        
        # If the task marked as done has a difficulty of 'Easy'
        if task_difficulty == 'EA':
            # XP gained is base XP
            xp = base_xp
        # Elif task difficulty medium
        elif task_difficulty == 'ME':
            xp = base_xp * 2
        # Elif task difficulty hard
        elif task_difficulty == 'HA':
            xp = base_xp * 3
        # Elif task difficulty ambitious
        elif task_difficulty == 'AM':
            xp = base_xp * 4
        # No else statement to make this quicker to modify if I ever change the difficulty system
        
        #  Get the current logged in user
        user = request.user.profile
        
        # Initialize leftover variable. This is used to 'save' any remaining xp
        # a user may have when levelling up, to count towards them getting the next level
        leftover = 0
        
        # The user can mark a task as done or not done
        # If it's done, they gain xp
        if task.done_status:
            user.exp_points += xp
            
            # Feedback to the user their xp gain
            messages.success(request, 'You completed a task and gained {} xp!'.format(xp))
            
            # Calculate any 'leftover' xp
            if user.exp_points >= user.xp_threshold:
                leftover = user.exp_points - user.xp_threshold
            
        # Else, they lose xp. This is here in case a user mistakingly marks a task as done
        # Honesty is key but monitoring the user's activities is beyond the scope of this app!
        else:
            # Get the current user's xp before any calculations are made
            # in case they lose a level
            current_xp = user.exp_points
            # Minus the xp value of the task from their current xp
            user.exp_points -= xp
            
            # Feedback to the user their xp loss
            messages.warning(request, 'You lost {} xp'.format(xp))
            
            # If the user now has less than 0 xp
            if user.exp_points < 0:
                # Minus a level
                user.level_rank -= 1
                # Set the new xp threshold of the new level
                user.xp_threshold -= base_xp_threshold
                # Set their new xp
                # If the user loses a level from undoing a task, they do not get set to 0
                # xp like if they lose a level from lost hp
                # Instead, they go 'back in time' and have the same xp they would of had
                # at the previous level before marking the task as done
                # e.g. a user on 20xp at level 2 marks an ambitious task (40xp) as undone
                # They go back to level 1 (100xp threshold), but with 80xp already attained
                user.exp_points = user.xp_threshold - current_xp
                
                # Feedback to the user their level loss
                messages.warning(request, 'You lost a level!')
            
        # If the user's xp has reached or exceeded their current xp_threshold
        if user.exp_points >= user.xp_threshold:
            # Reset experience points, but allow the user to retain full xp from a task
            # e.g. if a user completes an amibitous task (40xp) when they only need 10 to level up
            # they will have 30xp towards the next level
            user.exp_points = 0 + leftover
            # Increment the users level by 1
            user.level_rank +=1
            # Set the new xp_threshold
            # Each subsequent level gets harder to obtain!
            user.xp_threshold += base_xp_threshold
            
            # Feedback to the user
            messages.success(request, "Well done! You've just gained a level!")
    
          
         # Save the updated user instance  
        user.save()
        
        return redirect('tasks:get_tasks')
    
@login_required
def delete_task(request, task_id):
    """
    Allows a user to delete a task they created
    """
    # Get the task
    task = get_object_or_404(Task, pk=task_id)
    
    # Ensure only the user who created the task is able to delete it
    if not request.user == task.user:
        # Return a 404 page
        return render(request, '404.html')
    
    # If the user trying to delete a task is indeed the user who created the task,
    # allow them to carry out the action
    else:
        task.delete()
        return redirect('tasks:get_tasks')