from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.

# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             post_form.instance.author = request.user
#             post_form.save()
#             return redirect('authors:posts')
#     else:
#         post_form = PostForm()
    
#     return render(request, 'posts/post_form.html', {
#         'form': post_form,
#         'title': 'Add Post'
#     })

# add post using class based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('authors:posts')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# @login_required
# def edit_post(request, id):
#     post = Post.objects.get(pk=id)
#     post_form = PostForm(instance=post)
#     if request.method == 'POST':
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('authors:posts')
#     return render(request, 'posts/post_form.html', {
#         'form': post_form,
#         'title': 'Edit Post'
#     })

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('authors:posts')

# @login_required
# def delete_post(request, id):
#     post = Post.objects.get(pk=id)
#     post.delete()
#     return redirect('authors:posts')

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('authors:posts')