"""levelup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    # Since the accounts app path comes before the auth accounts path,
    # the accounts app path will be priority
    # path('accounts', include('accounts.urls')),
    path('sign_up/', accounts_views.register, name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls'))
]
