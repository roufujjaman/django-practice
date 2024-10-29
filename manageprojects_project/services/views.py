from django.shortcuts import render
from .models import Categories

# Create your views here.
def all_categoreis(request):
    return render(request, 'services/all_categories.html', {
        "categories": Categories.objects.all() 
    })