# Import Django components
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Import views
from . import views

urlpatterns = [
    # Default url, take user to index page
    path('', views.index, name='index'),
    # Admin url
    path('admin/', admin.site.urls),
    # Accounts app urls
    path('/', include('accounts.urls')),
    # Tasks app urls
    path('tasks/', include('tasks.urls')),
    # Stats app urls
    path('stats/', include('stats.urls')),
    # About url, go to the about page
    path('get_started/', views.get_started, name='get_started'),
    # Make a 'charge' to the user who goes through with a donation
    path('charge/', views.charge, name='charge'),
]

# When in development, append media files to urlpatterns containing MEDIA_URL
# and MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
