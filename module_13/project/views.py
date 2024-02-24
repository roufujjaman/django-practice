from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

class NewUser(forms.Form):
    name = forms.CharField(label="User Name", empty_value="Name")
    email = forms.EmailField(label="Email")

all_users = []

def home(request):
    return render(request, 'project/index.html')

def form(request):
    if request.method == 'POST':
        user = NewUser(request.POST)
        if user.is_valid():
            print(type(user))
            print(type(user.cleaned_data))

            name = user.cleaned_data['name']
            email = user.cleaned_data['email']
            all_users.append({
                'name': name,
                'email': email
                })
            return HttpResponseRedirect('/users')
        else:
            return render(request, 'project/form.html', {
                "form": user
            })
    return render(request, 'project/form.html', {
        "form": NewUser()
    })

def users(request):
    return render(request, 'project/users.html', {
        "users": all_users
        })