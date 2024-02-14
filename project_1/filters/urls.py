from django.urls import path
from . import views

app_name = "filters"
urlpatterns = [
    path("", views.home, name="home"),
    path("test_inheritance/", views.testInheritance, name="test_inheritance"),
    path("test_url/<slug:name><int:age>/", views.testUrl, name="test_url") 
]