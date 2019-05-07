from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.get_tasks, name='get_tasks'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('create_task', views.create_task, name='create_task'),
    path('done/<int:task_id>/<task_difficulty>/', views.toggle_done_status, name='toggle_done_status'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task')
]