from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, "filters/index.html", {
        "arr": ["a", "b", "c"],
        "today": datetime.now(),
        "emptyArr": []
    })
