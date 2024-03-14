from django.shortcuts import render
from django import forms

class newUser(forms.Form):
    username = forms.CharField(
        label="User Name",
        initial="John Doe",
        help_text="Enter Full Name"
    )
    useremail = forms.EmailField(
        label="Email"
    )
    age = forms.IntegerField(
        label="Age"
    )
    weight = forms.FloatField(
        label="Weight"
    )
    birthday = forms.DateField(
        label="Birthday",
        
        # use of widget
        widget=forms.DateInput(
            attrs={"type": "date"}
        )
    )
    sizeCHOICES = [("S", "SMALL"), ("M", "MEDIUM"), ("L", "LARGE")]
    size = forms.ChoiceField(
        label="T-Shirt",
        choices=sizeCHOICES
    )
    itemCHOICES = [(1, "PAPER"), (2, "PEN"), (3, "PENCIL"), (4, "ERASER")]
    items = forms.MultipleChoiceField(
        label="Gift",
        choices=itemCHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    check = forms.BooleanField(
        label="Agree"
    )

class newFile(forms.Form):
    username = forms.CharField(
        label="User Name"
    )
    file = forms.FileField(
        label="Upload File"
    )

all_users = []

def home(request):
    return render(request, 'project/index.html')

def form(request):
    if request.method == "POST":
        userForm = newUser(request.POST)
        if userForm.is_valid():
            all_users.append({
                "name": userForm.cleaned_data["username"],
                "email": userForm.cleaned_data["useremail"]
                })
        else:
            return render(request, 'project/form.html', {
                "newUser": userForm
            })
    return render(request, 'project/form.html', {
        "newUser": newUser()
    })

def file(request):
    if request.method == "POST":
        userForm = newFile(request.POST, request.FILES)
        if userForm.is_valid():
            file = userForm.cleaned_data['file']
            with open('upload/' + file.name, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        else:
            return render(request, 'project/file.html', {
                "fileForm": userForm
            })
    return render(request, 'project/file.html', {
        "fileForm": newFile()
    })

def users(request):
    return render(request, 'project/users.html', {
        "users": all_users
        })