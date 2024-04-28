from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_musicians(request):
    if request.method == 'POST':
        musician_form = forms.MusicianFrom(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
        else:
            return render(request, 'musicians/add_musicians.html', {
                'form': musician_form
            })
        
    return render(request, 'musicians/add_musicians.html', {
        'form': forms.MusicianFrom
    })