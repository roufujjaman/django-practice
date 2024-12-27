from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime

# Create your models here.
APOINTMENT_STATUS = (
    ("CM", "Completed"),
    ("PN", "Pending"),
    ("RN", "Running")
)

APOINTMENT_TYPES = (
    ("OF", "Offline"),
    ("ON", "Online")
)

class Apointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    apointment_types = models.CharField(choices=APOINTMENT_TYPES, max_length=2)
    apointment_status = models.CharField(choices=APOINTMENT_STATUS, max_length=2, default="PN")
    symptoms = models.TextField()
    time = models.OneToOneField(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor:\t{self.doctor.user.first_name}\nPatient:\t{self.patient.user.first_name}"