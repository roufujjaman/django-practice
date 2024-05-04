from django.shortcuts import render, redirect
from .forms import CategoryFrom

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = CategoryFrom(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
        else:
            return render(request, 'categories/add_category.html', {
                'form': category_form
            })
        
    return render(request, 'categories/add_category.html', {
        'form': CategoryFrom()
    })