from django.urls import path
from . import views

urlpatterns = [
    # path("", views.Home.as_view()),
    path("test", views.test)
]