import random
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

all_posts = list(Post.objects.all())

def home(request):
    context = {
        'posts': Post.objects.all(),
        'featured_post': Post.objects.last(),
        'random_posts': random.sample(all_posts, min(len(all_posts), 5)),
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def technology(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Technology',
    }
    return render(request, 'blog/tech.html', context)

def design(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Design',
    }
    return render(request, 'blog/design.html', context)

def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'blog/about.html', context)
