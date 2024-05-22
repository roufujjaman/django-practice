from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

# class bassed view 
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('authors:posts')
    else:
        post_form = PostForm()
    
    return render(request, 'posts/post_form.html', {
        'form': post_form,
        'title': 'Add Post'
    })
# class bassed view
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('authors:posts')
    return render(request, 'posts/post_form.html', {
        'form': post_form,
        'title': 'Edit Post'
    })

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('authors:posts')