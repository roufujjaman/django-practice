from django.shortcuts import render, redirect
from .forms import UserSignup, UserProfile
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html', {
        'title': 'Home'
    })

def signup(request):
    if request.method == 'POST':
        new_user_form = UserSignup(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            return redirect('home')
    else:
        new_user_form = UserSignup()
    return render(request, 'user_forms.html', {
        'form': new_user_form,
        'title': 'Create User'
    })

def signin(request):
    if request.method == 'POST':
        signin_user_form = AuthenticationForm(request, request.POST)
        if signin_user_form.is_valid():
            user_name = signin_user_form.cleaned_data['username']
            user_pass = signin_user_form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        signin_user_form = AuthenticationForm()

    return render(request, 'user_forms.html', {
        'form': signin_user_form,
        'title': 'Create User'
    })

@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Logged Out')
    return redirect('signin')

@login_required
def profile(request):
    if request.method == 'POST':
        profile_user_form = UserProfile(request.POST, instance=request.user)
        if profile_user_form.is_valid():
            profile_user_form.save()
            messages.success(request, 'Profile Modified Successfully')
            return redirect('profile')
        else:
            messages.warning(request, 'Could Not Modify The Profile')
    else:
        profile_user_form = UserProfile(instance=request.user)
    
    return render(request, 'user_forms.html', {
        'form': profile_user_form,
        'title': 'User Profile'
    })

@login_required
def password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return redirect('home')
    else:
        password_form = PasswordChangeForm(user=request.user)
    return render(request, 'user_forms.html', {
        'form': password_form,
        'title': 'Change Password'
    })