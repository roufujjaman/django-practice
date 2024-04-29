from django.shortcuts import render
from musicians.models import Musician

def home(request):
    
    # musicians = Musician.objects.all() # also works
    musicians = Musician.objects.prefetch_related('albums').all()
    return render(request, 'layout.html', {
        'musicians': musicians
    })