from django.shortcuts import render, redirect
from . import forms
from . import models

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

def edit_musicians(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianFrom(instance=musician)
    if request.method == "POST":
        musician_form = forms.MusicianFrom(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
        else:
            return render(request, 'musicians/add_musician.html', {
                'form': musician_form
            })

    return render(request, 'musicians/add_musicians.html', {
        'form': musician_form
    })

def delete_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')