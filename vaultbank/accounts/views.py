from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm, AccountForm, AddressForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import Transaction

from .models import Account, Address


@login_required(login_url='/account/login')
def home_account(request):
    account = Account.objects.get(user=request.user)
    return render(request, "accounts/account_home.html", 
                  {"account": account})

class AccountView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "accounts/account_home.html"
    context_object_name = "transactions"

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account = self.request.user.account
        )
        
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        print(start_date_str, end_date_str)
        return queryset

def create_account(request):
    user_form = UserForm()
    account_form = AccountForm()
    address_form = AddressForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        account_form = AccountForm(request.POST)
        address_form = AddressForm(request.POST)
        if all([user_form.is_valid(), account_form.is_valid(), address_form.is_valid()]):
            user = user_form.save(commit=True)

            account_form.instance.user = user
            account_form.instance.account_no = int(user.id) + 1000
            address_form.instance.user = user

            account_form.save()
            address_form.save()

            username = request.POST["username"]
            password = request.POST["password1"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

            messages.success(request, "Account Created Successfully")

            return redirect("account")

    return render(request, "accounts/form_create_account.html", {
        "UserForm": user_form,
        "AccountForm": account_form,
        "AddressForm": address_form
    })


def edit_account(request, id):

    user_form = UserForm(instance=User.objects.get(pk=id))
    Account_form = AccountForm(instance=Account.objects.get(pk=id))
    address_form = AddressForm(instance=Address.objects.get(pk=id))
    
    return render(request, "Account/Account_form.html", {
        "UserForm": user_form,
        "AccountForm": Account_form,
        "AddressForm": address_form
    })




def login_account(request):
    user_form = AuthenticationForm(request)
    
    if request.method == "POST":
        user_form = AuthenticationForm(request, request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("accounts:home")
            


    return render(request, "accounts/form_login.html", {
        "LoginForm": user_form
    })

def logout_account(reqeust):
    logout(request=reqeust)
    return redirect("accounts:login")

