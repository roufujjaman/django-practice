from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.



@login_required(login_url="/admin")
def by_user(request):
    if request.method == "GET":
        u = request.user
        role = u.roles.all()
        m = role.values_list("role", flat=True)

        if "architect" in m:
            return HttpResponse("working now")
        else:
            return HttpResponse("you are not authorized")


def home(request):
    return render(request, "users/user.html")
    