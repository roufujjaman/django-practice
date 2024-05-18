from django.shortcuts import render
from posts.models import Post

def home(request):
    all_post = Post.objects.all()
    for i in all_post:
        print(i.category)
    return render(request, 'home.html', {
        'posts': all_post
    })