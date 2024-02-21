from django.urls import path
from . import views

app_name = 'meals'
urlpatterns = [
    path('', views.home, name='home')
]