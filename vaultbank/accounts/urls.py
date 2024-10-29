from django.urls import path
from .views import create_account, authorized

urlpatterns = [
    path("", create_account, name=""),
    path("authorized", authorized)
]