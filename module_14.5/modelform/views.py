from django.shortcuts import render
from . import models
# Create your views here.


def home(request):
    return render(request, "project/modelform_home.html")


def model(request):
    if request.method == "POST":
        my_model = models.MyModel()
        my_model.name = request.POST["name"]
        my_model.size = request.POST["size"]
        my_model.date = request.POST["date"]
        print(my_model.name, my_model.size, my_model.date)
        my_model.save()
    return render(request, "project/model.html")

def model_entries(request):
    return render(request, "project/model_entries.html", {
        "entries": models.MyModel.objects.all()
    })