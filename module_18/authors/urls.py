from django.urls import path
from . import views

app_name = 'authors'
urlpatterns = [
    path('register', views.register_user, name='register_author'),
    path('login', views.login_user, name='login_author')
    
]