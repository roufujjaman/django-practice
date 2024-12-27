from django.contrib import admin
from .models import Apointment
# Register your models here.

class ApointmentAdmin(admin.ModelAdmin):
    list_display = ["doctor_name", "patient_name", "apointment_types", "apointment_status", "symptoms", "time", "cancel"]

    def patient_name(self, obj):
        return obj.patient.user.first_name
    
    def doctor_name(self, obj):
        return obj.doctor.user.first_name


admin.site.register(Apointment, ApointmentAdmin)
