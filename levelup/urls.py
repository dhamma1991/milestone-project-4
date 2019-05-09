from django.contrib import admin # Import admin to allow access to admin panel
from django.contrib.auth import views as auth_views # Import Django authorization views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from accounts import views as accounts_views
from stats import views as stats_views

urlpatterns = [
    # Default url, take user to index page
    path('', views.index, name='index'),
    # Admin url
    path('admin/', admin.site.urls),
    # Tasks url, get the user's tasks (or prompt them to login)
    path('tasks/', include('tasks.urls')),
    # Stats url, go to the stats page
    path('stats/', include('stats.urls')),
    # About url, go to the about page
    path('get_started/', views.get_started, name='get_started'),
    # Donate url, go to the donate page
    path('donate/', accounts_views.donate, name='donate'),
    # Make a 'charge' to the user who goes through with a donation
    path('charge/', views.charge, name='charge'),
    # Sign up url, go to the sign up page, post the form
    path('sign_up/', accounts_views.register, name='sign_up'),
    # Profile url, go to the user's profile page
    path('profile/', accounts_views.profile, name='profile'),
    # Login url, default Django login, point Django towards the template in the accounts app
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # Logout url, default Django logout, point Django towards the template
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # Password Reset URLs 
    # These are mostly Django defaults, although Django must be pointed
    # Towards the 'accounts' directory, by default it will look for a 'registration'
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',
        # Set the email template and the email subject
        email_template_name = 'accounts/password_reset_email.html',
        subject_template_name = 'accounts/password_reset_subject.txt'), 
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), 
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), 
        name='password_reset_complete'),
    # /Password Reset URLs
    
]

# When in development, append media files to urlpatterns containing MEDIA_URL
# and MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
