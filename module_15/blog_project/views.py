from django.shortcuts import render
from posts.models import Post
def home(request):
    all_post = Post.objects.all()
    return render(request, 'home.html', {
        "posts": all_post
    })