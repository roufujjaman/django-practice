from django.shortcuts import render
from django.views.generic import CreateView
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout



# Create your views here.

class RegisterUserView(CreateView):
    model = forms.User
    fields = ['username', 'first_name', 'password']
    forms_class = forms.RegisterUserForm
    template_name = 'author/author_forms.html'
    success_url = 'author'


def author_login(request):
    author_login_form = AuthenticationForm()
    print(request.headers) 
    if request.method == 'POST':
        author_login_form = AuthenticationForm(request=request, data=request.POST)
        if author_login_form.is_valid():
            user = authenticate(
                username=author_login_form.cleaned_data['username'],
                password=author_login_form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
    return render(request, 'author/author_forms.html', {
        'form': author_login_form
    })


def author_logout(request):
    pass
