from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "project/layout.html", {
        "name": "Project-001",
    })