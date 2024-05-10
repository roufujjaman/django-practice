from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . import forms

def signup(request):
    if request.method == 'POST':
        register_form = forms.RegisterFrom(request.POST)
        if register_form.is_valid():
            messages.success(request, 'Account Created Successfully')
            register_form.save(commit=True)
        else:
            return render(request, 'first_app/signup.html', {
                'form': register_form
            })        
    return render(request, 'first_app/signup.html', {
        'form': forms.RegisterFrom()
    })

def signin(request):
    if request.method == 'POST':
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
            return render()

    return render(request, 'first_app/signin.html', {
        'form': AuthenticationForm()
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