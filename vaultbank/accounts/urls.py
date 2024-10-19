from django.urls import path
from .views import create_account

urlpatterns = [
    path("", create_account, name="")
]