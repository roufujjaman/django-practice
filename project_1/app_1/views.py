from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    now = datetime.datetime.now()
    return render(request, 'app_1/body.html', {
        "newyear": now.month == 1 and now.day == 1
    })