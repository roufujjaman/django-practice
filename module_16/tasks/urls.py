from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('show_tasks/', views.show_tasks, name='show_tasks') 
]