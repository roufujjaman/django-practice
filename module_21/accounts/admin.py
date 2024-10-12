from django.contrib import admin
from .models import UserAccount, UserAddress
# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["user", "account_type", "balance"]

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ["user", "street_address"]    


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(UserAddress, UserAddressAdmin)