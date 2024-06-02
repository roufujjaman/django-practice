from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [
    path('', views.RegisterUserView.as_view(), name='register_user')
]