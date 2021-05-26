"""User's URL patterns for users"""

from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # Default auth URLs
    path('', include('django.contrib.auth.urls')),
    # Register an new account
    path('register/', views.register, name='register'),
]