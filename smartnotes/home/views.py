from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "home/signup.html"
    success_url = "smart/notes"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("smart/notes")
        return super().get(self, request, *args, **kwargs)

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {"today": datetime.now()}

class LoginInterfaceView(LoginView):
    template_name = "home/login.html"

class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"


# class AuthorizedView(LoginRequiredMixin, TemplateView):
#     template_name = "home/authorized.html"
#     login_url = "/admin"