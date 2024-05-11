from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from . import forms

def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
        
    if request.method == 'POST':
        register_form = forms.RegisterFrom(request.POST)
        if register_form.is_valid():
            messages.success(request, 'Account Created Successfully')
            register_form.save(commit=True)
    else:
        register_form = forms.RegisterFrom()

    return render(request, 'first_app/signup.html', {
        'form': register_form
    })

def signin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    
    elif request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_password = login_form.cleaned_data['password']
            print(user_password)
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        login_form = AuthenticationForm()

    return render(request, 'first_app/signin.html', {
        'form': login_form
    })


def signout(request):
    logout(request)
    return redirect('login_user')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'first_app/profile.html', {
            'user': request.user
        })
    return redirect('login_user')

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    elif request.method == 'POST':
        change_password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)
            return redirect('profile')
    else:
        change_password_form = PasswordChangeForm(user=request.user)
    
    return render(request, 'first_app/changepassword.html', {
        'form': change_password_form
    })

def change_user_date(request):
    if request.user.is_authenticated:
        user_form = forms.ChangeUserDataForm(instance=request.user)
    
    if request.method == 'POST':
        user_form = forms.ChangeUserDataForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'User Data Changed Successfully')
            return redirect('profile')
        
    return render(request, 'first_app/changeuserdata.html', {
        'form': user_form
    })