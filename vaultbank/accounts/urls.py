from django.urls import path
from .views import create_account, authorized, testpost, edit

urlpatterns = [
    path("", create_account, name=""),
    path("authorized", authorized),
    path("<int:id>", edit),
    path("testpost", testpost),
]