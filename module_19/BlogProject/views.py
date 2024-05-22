from django.shortcuts import render
from posts.models import Post, Category

def home(request, cat = None):
    all_post = Post.objects.all()
    if cat is not None:
        category = Category.objects.get(slug=cat)
        all_post = Post.objects.filter(category=category)
    return render(request, 'home.html', {
        'posts': all_post
    })