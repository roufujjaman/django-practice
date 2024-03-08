from django.shortcuts import render
from django import forms

class newUser(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput
    )

all_users = []

def home(request):
    return render(request, 'project/index.html')

def form(request):
    return render(request, 'project/form.html', {
        "newUser": newUser()
    })

def users(request):
    return render(request, 'project/users.html', {
        "users": all_users
        })