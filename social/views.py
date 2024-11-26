from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib import messages


# Home page v
def home(request):
    return render(request, 'home.html')

# Only accessible if the user is logged in
@login_required
def feed(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts ordered by date
    return render(request, 'feed.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

def booking(request):
    
    return render(request, 'booking.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user) #Autologin after user reg
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})