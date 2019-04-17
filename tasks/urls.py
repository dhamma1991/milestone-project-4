from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('tasks/', views.get_tasks, name='get_tasks'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('create_task', views.create_task, name='create_task'),
    path('tasks/done/<int:task_id>/<task_difficulty>/', views.toggle_done_status, name='toggle_done_status'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task')
]