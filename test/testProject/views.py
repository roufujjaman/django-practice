from django.shortcuts import render


def home(request, name):
    return render(request, 'home.html', {
        'name': name
    })