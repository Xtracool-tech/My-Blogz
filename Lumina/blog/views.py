import random
from django.shortcuts import render
from .models import Post

all_posts = list(Post.objects.all())

def home(request):
    context = {
        'posts': Post.objects.all(),
        'featured_post': Post.objects.last(),
        'random_posts': random.sample(all_posts, min(len(all_posts), 5)),
    }
    return render(request, 'blog/home.html', context)
