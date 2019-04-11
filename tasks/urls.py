from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    # path('<uuid:pk>/add_task', views.create_or_edit_task, name='create_or_edit_task')
    path('create_task', views.create_task, name='create_task')
]