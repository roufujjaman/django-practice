from django.shortcuts import render, HttpResponse
from .forms import UserForm, AccountsForm, AddressForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
# class AccountCreateView(CreateView):
#     form_class = {"account": AccountsForm,
#                     "address": AddressForm}
#     template_name = "accounts/accounts_form.html"


def create_account(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        accounts_form = AccountsForm(request.POST)
        address_form = AddressForm(request.POST)
        print(request.POST)


        if all([user_form.is_valid(), accounts_form.is_valid(), address_form.is_valid()]):
            
            user = user_form.save()
    
            accounts_form.instance.user = user
            accounts_form.instance.account_no = int(user.id) + 1000
            address_form.instance.user = user

            accounts_form.save()
            address_form.save()
            
            username = request.POST["username"]
            password = request.POST["password1"]

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)

    else:
        user_form = UserForm()
        accounts_form = AccountsForm()
        address_form = AddressForm()

    return render(request, "accounts/accounts_form.html", {
        "UserForm": user_form,
        "AccountsForm": accounts_form,
        "AddressForm": address_form
    })

@login_required
def authorized(request):
    return HttpResponse("User Authenticated")