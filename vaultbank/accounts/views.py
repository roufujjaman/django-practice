from django.shortcuts import render, HttpResponse
from .forms import UserForm, AccountsForm, AddressForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Accounts, Address

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

    return render(request, "accounts/accounts_form.html", {
        "UserForm": user_form,
        "AccountsForm": accounts_form,
        "AddressForm": address_form
    })


@login_required
def authorized(request):
    return HttpResponse("User Authenticated")

def testpost(request):
    if request.method == "POST":
        print(request.POST)
    
    return render(request, "accounts/post_test.html")

def edit(request, id):

    user_form = UserForm(instance=User.objects.get(pk=id))
    accounts_form = AccountsForm(instance=Accounts.objects.get(pk=id))
    address_form = AddressForm(instance=Address.objects.get(pk=id))
    
    return render(request, "accounts/accounts_form.html", {
        "UserForm": user_form,
        "AccountsForm": accounts_form,
        "AddressForm": address_form
    })
