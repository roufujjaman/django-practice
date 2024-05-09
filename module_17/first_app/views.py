from django.shortcuts import render

def signup(request):
    return render(request, 'first_app/signup.html')