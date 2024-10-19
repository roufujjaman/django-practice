from django.shortcuts import render
from django.views.generic import CreateView
from .forms import AccountsForm, AddressForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# class AccountCreateView(CreateView):
#     form_class = {"account": AccountsForm,
#                     "address": AddressForm}
#     template_name = "accounts/accounts_form.html"

def create_account(request):
    return render(request, "accounts/accounts_form.html", {"user": UserCreationForm, "accounts_form": AccountsForm, "address_form": AddressForm})