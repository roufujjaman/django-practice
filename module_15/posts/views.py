from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        else:
            return render(request, 'posts/add_post.html', {
                "form": post_form
            })
    
    return render(request, 'posts/add_post.html', {
        "form": PostForm()
    })