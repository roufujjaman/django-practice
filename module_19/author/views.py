from django.shortcuts import render
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.
def register_user(request):
    return render(request, 'author/user_forms.html', {
        'form': UserCreationForm()
    })