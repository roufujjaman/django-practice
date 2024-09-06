from django.urls import path
from . import views

app_name = 'authors'
urlpatterns = [
    path('register/', views.register_user, name='register_author'),
    path('login/', views.UserLoginView.as_view(), name='login_author'),
    path('logout/', views.LogoutView.as_view(), name='logout_author'),
    path('profile/', views.profile, name='profile'),
    path('password/', views.change_password, name='password'),
    path('my_post/', views.authors_posts, name='posts')
]