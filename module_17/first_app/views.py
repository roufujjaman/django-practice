from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # register_form.save(commit=False)
            messages.success(request, 'Account created successfully')
            register_form.save()
        else:
            return render(request, 'first_app/home.html', {
                'form': register_form
            })
        
    return render(request, 'first_app/home.html', {
        'form': RegisterForm()
    })