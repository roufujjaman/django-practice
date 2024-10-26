from django.shortcuts import render
from django.http import JsonResponse
from .models import Projects
from django.core import serializers


# Create your views here.
def home(request):
    # projects = serializers.serialize('json', Projects.objects.all())
    return render(request, "projects/home.html", {
        "projects": Projects.objects.all()
    })