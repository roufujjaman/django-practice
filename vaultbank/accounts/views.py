from django.shortcuts import render, HttpResponse
from .forms import UserForm, AccountsForm, AddressForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

def create_account(request):
    user_form = UserForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Account Created Successfully")    
        else:
            errors = user_form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "accounts/accounts_form.html", {
        "UserForm": user_form
    })


@login_required
def authorized(request):
    return HttpResponse("User Authenticated")

def testpost(request):
    if request.method == "POST":
        print(request.POST)
    
    return render(request, "accounts/post_test.html")
