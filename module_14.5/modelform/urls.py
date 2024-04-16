from django.urls import path
from . import views

app_name = "modelform"
urlpatterns = [
    path("", views.home, name="home"),
    path("model/", views.model, name="model"),
    path("model_entries/", views.model_entries, name="model_entries"),
    path("get_by_id/<int:id>/", views.get_by_id, name="get_by_id")
]