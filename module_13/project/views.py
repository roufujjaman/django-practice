from django.shortcuts import render
from django import forms

class newUser(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput
    )
    email = forms.EmailField(
        label="Email",
        required=False,
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
        required=False,
        widget=forms.TextInput(attrs={
            "class": "red",
            "placeholder": "is it red really?"
            })
    )
    def clean_fullname(self):
        valfullname = self.cleaned_data["fullname"]
        if len(valfullname) < 10:
            raise forms.ValidationError("Not Enough Charecters(min 10 characters)")
            print("--came here--")
        return valfullname

all_users = []

def home(request):
    return render(request, 'project/index.html')

def form(request):
    if request.method == "POST":
        form = newUser(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            return render(request, "project/form.html", {
                "newUser": form
            })
    return render(request, "project/form.html", {
        "newUser": newUser
        })

def users(request):
    return render(request, 'project/users.html', {
        "users": all_users
        })