from django.shortcuts import render, redirect
from .forms import AuthorRegistrationForm, ChangeUserDataForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post


from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        registration_form = AuthorRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('home')
    else:
        registration_form = AuthorRegistrationForm()

    return render(request, 'authors/author_forms.html', {
        'form': registration_form,
        'title': 'Author Registration'
    })

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                # messages.success(request, 'Logged In Successfully')
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'authors/author_forms.html', {
        'form': form,
        'title': 'Author Login'
    })

class UserLoginView(LoginView):
    template_name = 'authors/author_forms.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in Unsuccessful')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Author Login'
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy('home')

# @login_required
# def logout_user(request):
#     logout(request)
#     return redirect('authors:login_author')


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserDataForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('home')
    else:
        profile_form = ChangeUserDataForm(instance=request.user)
    return render(request, 'authors/author_forms.html', {
        'form': profile_form,
        'title': 'User Profile',
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.POST, request.user)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, password_form.user)
            return redirect('authors:profile')
    else:
        password_form = PasswordChangeForm(request.user)

    return render(request, 'authors/author_forms.html', {
        'form': password_form,
        'title': 'Change Password'
    })

@login_required
def authors_posts(request):
    all_post = Post.objects.filter(author=request.user)
    return render(request, 'authors/all_post.html', {
        'posts': all_post,
        'title': 'My Posts'
    })