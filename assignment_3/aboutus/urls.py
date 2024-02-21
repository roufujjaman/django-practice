from django.urls import path
from . import views

app_name = 'aboutus'
urlpatterns = [
    path('', views.home, name='home')
]