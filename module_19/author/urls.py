from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [
    path('', views.register_user, name='register_user')
]