from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

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


def edit_post(request, id):
    post = Post.objects.get(pk=id)
    post_form = PostForm(instance=post)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
        
    return render(request, 'posts/add_post.html', {
        "form": post_form
    })

def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')