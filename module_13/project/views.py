from typing import Any
from django.shortcuts import render
from django import forms

def home(request):
    return render(request, "project/index.html")


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


all_users = []

def form(request):
    if request.method == "POST":
        userForm = newUser(request.POST)
        if userForm.is_valid():
            all_users.append({
                "name": userForm.cleaned_data["username"],
                "email": userForm.cleaned_data["useremail"]
                })
        else:
            return render(request, "project/form.html", {
                "newUser": userForm
            })
    return render(request, "project/form.html", {
        "newUser": newUser()
    })

class newFile(forms.Form):
    username = forms.CharField(
        label="User Name"
    )
    file = forms.FileField(
        label="Upload File"
    )

def file(request):
    if request.method == "POST":
        userForm = newFile(request.POST, request.FILES)
        if userForm.is_valid():
            file = userForm.cleaned_data["file"]
            with open("upload/" + file.name, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        else:
            return render(request, "project/file.html", {
                "fileForm": userForm
            })
    return render(request, "project/file.html", {
        "fileForm": newFile()
    })

class formValidation(forms.Form):
    username = forms.CharField(
        label="User Name"
    )
    email = forms.EmailField(
        label="Email"
    )
    # approach 1

    # def clean_username(self):
    #     val = self.cleaned_data["username"]
    #     if len(val) < 5:
    #         raise forms.ValidationError("username must be more than 5 charecters")
    #     return val

    # def clean_email(self):
    #     val = self.cleaned_data["email"]
    #     if ".edu" not in val:
    #         raise forms.ValidationError("email must be an .edu")
    #     return val
    
    # approach 2

    def clean(self):
        cleaned_date = super().clean()
        val1 = self.cleaned_data["username"]
        val2 = self.cleaned_data["email"]

        if len(val1) < 5:
            raise forms.ValidationError("username must be >5 characters")
        if ".edu" not in val2:
            raise forms.ValidationError("email must be a '.edu'")
 
def validation(request):
    if request.method == "POST":
        userForm = formValidation(request.POST)
        if userForm.is_valid():
            print(userForm.cleaned_data["email"])
        else:
            return render(request, "project/validation.html", {
                "validationForm": userForm
            })
    return render(request, "project/validation.html", {
        "validationForm": formValidation()
    })

def users(request):
    return render(request, "project/users.html", {
        "users": all_users
        })