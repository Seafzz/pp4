from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('create-post/', views.create_post, name='create_post'),
]