from django.urls import path
from .views import create_account, authorized, testpost

urlpatterns = [
    path("", create_account, name=""),
    path("authorized", authorized),
    path("testpost", testpost)
]