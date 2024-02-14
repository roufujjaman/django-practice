from django.shortcuts import render

# Create your views here.
def body(request):
    return render(request, 'filters/body.html', {
        "style": { 
            "item": "box", # css/html class name
            "topic": "topic-text"
            },
        "greet": "hello world",
        "age": 28,
        "num": [123, 123, 123, 123]
    })