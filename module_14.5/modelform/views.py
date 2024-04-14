from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "project/modelform_home.html")


def model(request):
    pass