from django.urls import path, include
from .views import PatientViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", PatientViewset)

urlpatterns = [
    path("", include(router.urls)),
]

