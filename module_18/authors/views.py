from django.shortcuts import render, redirect
from .forms import AuthorRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

    return render(request, 'author_forms.html', {
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
    
    return render(request, 'author_forms.html', {
        'form': form,
        'title': 'Author Login'
    })

def logout_user(request):
    logout(request)
    return redirect('home')
                
