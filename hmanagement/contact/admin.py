from django.contrib import admin
from .models import ContactUs
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "phone", "problem"]

    verbose_name_plural = "Contact"
    pass


admin.site.register(ContactUs, ContactUsAdmin)