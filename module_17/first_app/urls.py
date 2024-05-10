from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='register_user'),
    path('signin/', views.signin, name='login_user'),
    path('signout/', views.signout, name='logout_user'),
    path('profile', views.profile, name='profile')
]