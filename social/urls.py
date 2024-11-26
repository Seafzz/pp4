from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
    path('create-post/', views.create_post, name='create_post'),
    path('booking/', views.booking, name='booking'),
    path('register/', views.register, name='register'),
]