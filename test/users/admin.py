from django.contrib import admin
from . import models

class RoelsAdmin(admin.ModelAdmin):
    list_display = ("id", "role", "number", "user")

# Register your models here.
admin.site.register(models.Roles, RoelsAdmin)