from django.contrib import admin

from . import models

# Register your models here.
class MusiciansAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email')
    list_display_links = ('email',)
admin.site.register(models.Musicians, MusiciansAdmin)