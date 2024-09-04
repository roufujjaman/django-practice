from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('add/', views.AddPostCreateView.as_view(), name='add'),
    path('edit/<int:id>/', views.edit_post, name='edit'),
    path('delete/<int:id>/', views.delete_post, name='delete')
]