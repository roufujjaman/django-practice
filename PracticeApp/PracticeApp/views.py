from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save(commit=True)
    else:
        user_form = UserCreationForm()
    
    return render(request, 'user.html', {
        'form': user_form
    })