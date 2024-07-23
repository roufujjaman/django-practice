from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

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

def signin(request):
    if request.method == 'POST':
        user_form = AuthenticationForm(request=request, data=request.POST)
        if user_form.is_valid():
            user_name = user_form.cleaned_data['username']
            user_pass = user_form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                print('log in successfull')
                return
            else:
                print('log in unsuccessfull')
    else:
        user_form = AuthenticationForm()

    return render(request, 'user.html', {
        'form': user_form
    })