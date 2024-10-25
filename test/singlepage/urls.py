from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("section/<int:num>", views.section, name="section"),
    path("scroll/", views.scroll, name="scroll"),
    path("posts", views.post, name="posts"),
    path("animation", views.animation, name="animation"),
    path("react", views.react, name="react")
]