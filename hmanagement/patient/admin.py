from django.contrib import admin
from .models import Patient
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ["phone", "image", "first_name"]



admin.site.register(Patient, PatientAdmin)