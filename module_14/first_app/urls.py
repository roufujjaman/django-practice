from django.urls import path
from . import views

app_name = "first_app"
urlpatterns=[
    path("", views.home, name="home"),
    path("add", views.add_student, name="add_student"),
    path("delete/<int:roll>", views.delete_student, name="delete_student")
]