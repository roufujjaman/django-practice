from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_account, name="account"),
    path("create", views.create_account, name="create"),
    path("login", views.login_account, name="login"),
    path("logout", views.logout_account, name="logout"),
    path("<int:id>", views.edit_account, name=""),
]