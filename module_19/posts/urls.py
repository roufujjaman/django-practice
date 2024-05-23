from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # path('add/', views.add_post, name='add'),
    path('add', views.AddPostCreateView.as_view(), name='add'),
    # path('edit/<int:id>/', views.edit_post, name='edit'),
    path('edit/<int:id>/', views.EditPostView.as_view(), name='edit'),
    # path('delete/<int:id>/', views.delete_post, name='delete')
    path('delete/<int:id>/', views.DeletePostView.as_view(), name='delete')
]