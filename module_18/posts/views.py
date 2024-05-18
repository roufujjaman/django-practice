from django.shortcuts import render, redirect
from .forms import PostForm
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            print(request.user)
            post_form.save()
            return redirect('home')
    else:
        post_form = PostForm()
    
    return render(request, 'posts/add_post_form.html', {
        'form': post_form,
        'title': 'Add Post'
    })