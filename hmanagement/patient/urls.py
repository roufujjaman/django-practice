from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("list", views.PatientViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", views.RegistrationAPIView.as_view())
]

