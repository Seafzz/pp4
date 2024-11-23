from django.shortcuts import render
from .models import Post
from .forms import PostForm

def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'social/feed.html', {'posts': posts})

