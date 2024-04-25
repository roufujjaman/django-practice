from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.
def add_profile(request):
    return render(request, 'profiles/add_profile.html', {
        "form": ProfileForm()
    })