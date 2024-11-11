from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm, AccountsForm, AddressForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import Accounts, Address


@login_required(redirect_field_name="login")
def home_account(request):
    account = Accounts.objects.filter(user=request.user)
    return render(request, "accounts/accounts_home.html", 
                  {"account": account})

def create_account(request):
    user_form = UserForm()
    accounts_form = AccountsForm()
    address_form = AddressForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        accounts_form = AccountsForm(request.POST)
        address_form = AddressForm(request.POST)
        if all([user_form.is_valid(), accounts_form.is_valid(), address_form.is_valid()]):
            user = user_form.save(commit=True)

            accounts_form.instance.user = user
            accounts_form.instance.account_no = int(user.id) + 1000
            address_form.instance.user = user

            user_form.save()
            accounts_form.save()
            address_form.save()

            username = request.POST["username"]
            password = request.POST["password1"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

            messages.success(request, "Account Created Successfully")

            return redirect("authorized")

    return render(request, "accounts/accounts_form.html", {
        "UserForm": user_form,
        "AccountsForm": accounts_form,
        "AddressForm": address_form
    })


def edit_account(request, id):

    user_form = UserForm(instance=User.objects.get(pk=id))
    accounts_form = AccountsForm(instance=Accounts.objects.get(pk=id))
    address_form = AddressForm(instance=Address.objects.get(pk=id))
    
    return render(request, "accounts/accounts_form.html", {
        "UserForm": user_form,
        "AccountsForm": accounts_form,
        "AddressForm": address_form
    })




def login_account(request):
    if request.method == "POST":
        user_form = AuthenticationForm(request, request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("looged in")
                return redirect("")


    return render(request, "accounts/authentication_form.html", {
        "LoginForm": AuthenticationForm
    })

def logout_account(reqeust):
    logout(request=reqeust)

    return redirect("login")

