from django.shortcuts import render
from musicians.models import Musician
from albums.models import Album

def home(request):
    
    musicians = Musician.objects.prefetch_related('album_set').all()
    print(musicians.all())
    return render(request, 'layout.html', {
        'musicians': musicians
    })