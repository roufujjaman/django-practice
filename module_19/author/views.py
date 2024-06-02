from django.shortcuts import render
from django.views.generic import CreateView
from . import forms



# Create your views here.

class RegisterUserView(CreateView):
    model = forms.User
    fields = ['username', 'first_name', 'password']
    forms_class = forms.RegisterUserForm
    template_name = 'author/author_forms.html'
    success_url = 'author'