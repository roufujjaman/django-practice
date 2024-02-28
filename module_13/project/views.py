from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

# class NewUser(forms.Form):
#     name = forms.CharField(label="User Name", empty_value="Name")
#     email = forms.EmailField(label="Email")
#     age = forms.IntegerField(label="Age")
#     weight = forms.FloatField(label="Weight")
#     SIZE_CHOICES = [("S", "Small"), ("L", "Large"), ("XL", "Extra Large")]
#     size = forms.ChoiceField(label="Size", choices=SIZE_CHOICES)

all_users = []

def home(request):
    return render(request, 'project/index.html')

def form(request):
    if request.method == "POST":
        file = request.FILES["file"]
        with open('./upload/' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print(file)
        return render(request, "project/form.html")
    

    return render(request, "project/form.html")

def users(request):
    return render(request, 'project/users.html', {
        "users": all_users
        })