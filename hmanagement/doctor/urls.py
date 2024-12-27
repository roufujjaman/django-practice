from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("list", views.DoctorViewset)
router.register("specialization", views.SpecializationViewset)
router.register("available_time", views.DesignationViewset)
router.register("designation", views.AvailableTimeViewset)
router.register("review", views.ReviewViewset)

urlpatterns = [
    path("", include(router.urls))
]

