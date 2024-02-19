from django.shortcuts import render


def home(request):
    return render(request, 'restaurantX\home.html')


def meals(request):
    return render(request, 'meals/meals.html')