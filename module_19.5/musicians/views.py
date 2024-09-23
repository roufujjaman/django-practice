from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    response = HttpResponse("working")
    response.set_cookie('time', 'set', max_age=60)
    return response