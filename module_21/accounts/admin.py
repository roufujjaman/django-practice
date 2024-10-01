from django.contrib import admin
from .models import UserAccount
# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    fields = (("user", "account_type"), "birth_date")
    list_displa = ["user", "account_type", "balance"]


admin.site.register(UserAccount, UserAccountAdmin)