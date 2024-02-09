from django.shortcuts import render

# Create your views here.
tasks = ["foo", "bar", "baz"]

def home(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")