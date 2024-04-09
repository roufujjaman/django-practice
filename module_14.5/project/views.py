from django.shortcuts import render
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(
        label="Full Name",
        max_length="150",
        widget=(forms.TextInput(attrs={"class": "max-w-sm mx-auto"}))
    )

def home(request):
    return render(request, "project/layout.html")

def form(request):
    return render(request, "project/form.html", {
        "userForm": UserForm()
    })