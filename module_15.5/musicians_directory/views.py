from django.shortcuts import render
from musicians.models import Musician

def home(request):
    
    # musicians = Musician.objects.prefetch_related('albums').all()
    musicians = Musician.objects.all()
    print(musicians)
    return render(request, 'layout.html', {
        'musicians': musicians
    })