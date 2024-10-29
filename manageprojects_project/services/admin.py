from django.contrib import admin
from .models import Categories, SubCategories

# Register your models here.
class CategoriesModel(admin.ModelAdmin):
    list_display = ["order", "name", "duration_days_default" ]



admin.site.register(Categories, CategoriesModel)
admin.site.register(SubCategories)