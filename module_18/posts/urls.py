from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('add/', views.add_post, name='add_post'),

]