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
# Import Django authorization views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    # Since the accounts app path comes before the auth accounts path,
    # the accounts app path will be priority
    path('sign_up/', accounts_views.register, name='sign_up'),
    path('profile/', accounts_views.profile, name='profile'),
    # URL for login, point Django towards the template in the accounts app
    # using template_name
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]

# When in development, append media files to urlpatterns containing MEDIA_URL
# and MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
