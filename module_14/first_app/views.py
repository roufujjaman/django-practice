from django.shortcuts import render, redirect
from . import models
from . import forms as appforms
# Create your views here.
def home(request):
    return render(request, "project/students.html", {
        "students": models.Student.objects.all()
    })

def delete_student(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("first_app:home")

def add_student(request):
    return render(request, "project/addstudent.html", {
        "studentform": appforms.StudentForm
    })