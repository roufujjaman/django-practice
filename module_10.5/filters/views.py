from django.shortcuts import render
from datetime import datetime


# Create your views here.
def body(request):
    return render(request, 'filters/body.html', {
        "style": { 
            "item": "box", # css/html class name
            "topic": "topic-text"
            },
        "greet": "hello world",
        "age": 28,
        "string1": "i'm a string with 'quotes'",
        "name1": "bruyne",
        "string2": "i'm a string without 'spaces'",
        "today": datetime.today(),
        "arr": ["A", "99", "10", "35", "X"],
        "players": [
            {"name": "bruyne", "age": 30},
            {"name": "haland", "age": 22},
            {"name": "foden", "age": 25}
        ],
        "filesize": 10241024,
        "numbers": range(1, 10),
        "falgun": datetime(2024, 2, 14),
        "locations": ['bangladesh', ['dhaka', ['uttara', 'banani']], 'sylhet',['airport road']],
        "longtext": "this is not a long text to be honest"
    })