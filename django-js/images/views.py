from django.shortcuts import render, HttpResponse
import os
# Create your views here.

def home(request):
    if request.method == "POST":
        for filename, file in request.FILES.items():
            ext = request.FILES[filename].name.split(".")[-1:][0]
            new_file_name = filename + "." + ext
            with open(f"upload/{new_file_name}", "wb+") as f:
                for chunk in file:
                    f.write(chunk)
    return render(request, "images/index.html")