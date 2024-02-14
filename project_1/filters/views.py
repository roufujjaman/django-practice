from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, "filters/index.html", {
        "arr": ["a", "b", "c"],
        "today": datetime.now(),
        "emptyArr": [],
        "players": [{"name": "foden", "age": 23},
                    {"name": "bruyne", "age": 32},
                    {"name": "grealish", "age": 28}],
        "h1": "<p> this is an escape tag</p>",
    })


def testInheritance(request):
    return render(request, "filters/testInheritance.html")

def testUrl(request):
    return render(request, "filters/testUrl.html", {
        "args": request.GET
    })