from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('add/', views.AddPostCreateView.as_view(), name='add'),
    path('edit/<int:id>/', views.EditPostView.as_view(), name='edit'),
    path('delete/<int:id>/', views.DeletePostView.as_view(), name='delete')
]