from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets
# Create your views here.

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
