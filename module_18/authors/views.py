from django.shortcuts import render
from .forms import AuthorRegistrationForm
from django.contrib.auth import authenticate

# Create your views here.

def register_user(request):

    registration_form = AuthorRegistrationForm()
    return render(request, 'author_forms.html', {
        'form': registration_form,
        'title': 'Registration Author'
    })

def login_user(request):
    pass