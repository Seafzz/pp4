from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
    path('create-post/', views.create_post, name='create_post'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login, name='login'),
]