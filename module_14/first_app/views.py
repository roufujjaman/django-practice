from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    return render(request, "project/students.html", {
        "students": models.Student.objects.all()
    })