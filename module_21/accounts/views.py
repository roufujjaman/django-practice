from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm
# Create your views here.


class UserRegistrationView(FormView):
    template_name = "accounts/account_registration.html"
    form_class = UserRegistrationForm