from django.urls import path, include
from .views import ServiceViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", ServiceViewset)

urlpatterns = [
    path("", include(router.urls))
]