from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.



class Home(TemplateView):
    template_name = 'musicians/musicians.html'
    extra_context = {
        'musicians': models.Musicians.objects.all()
    }