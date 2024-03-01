from django.shortcuts import render
from django import forms

class newUser(forms.Form):
    fullname = forms.CharField(
        label="Full name",
        max_length=5,
    )
    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(attrs={"class": "red"})
    )
    country = forms.CharField(
        label="Country",
        initial="Bangladesh",
        disabled=True
    )
    file = forms.FileField(
        label="File",
        required=False
    )
    color = forms.CharField(
        label="Color Test",
        widget=forms.TextInput(attrs={
            "class": "red",
            "placeholder": "is it red really?"
            })
    )

all_users = []

def home(request):
    return render(request, 'project/index.html')

def form(request):
    if request.method == "POST":
        pass
    return render(request, "project/form.html", {
        "newUser": newUser
        })

def users(request):
    return render(request, 'project/users.html', {
        "users": all_users
        })