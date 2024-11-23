"""
URL configuration for devconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from social import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', views.feed, name='feed'),
    path('create-post/', views.create_post, name='create_post'),
    path('booking/', views.booking, name='booking'),
    path('', views.home, name='home'),

    # Login URL
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Default Django login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Default Django logout view
]