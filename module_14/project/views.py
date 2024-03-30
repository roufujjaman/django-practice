from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "<h1><a href='/first_app'>First App</a><h1>"
    )