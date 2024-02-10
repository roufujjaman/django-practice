from django.urls import path
from . import views

app_name = "app_1"
urlpatterns = [
    path("", views.home, name="index"),
]