from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('tasks/', views.get_tasks, name='get_tasks'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('create_task', views.create_task, name='create_task'),
    path('done/<int:task_id>', views.toggle_done_status, name='toggle_done_status')
]