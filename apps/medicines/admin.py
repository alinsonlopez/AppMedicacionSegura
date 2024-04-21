from django.contrib import admin
from .models import Categories, Medicines


# Register your models here.

@admin.register(Categories, Medicines)
class BaseAdminRegister(admin.ModelAdmin):
    pass
