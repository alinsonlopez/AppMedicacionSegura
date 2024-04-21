from django.contrib import admin
from .models import Symptoms, Medicines


# Register your models here.

@admin.register(Symptoms, Medicines)
class BaseAdminRegister(admin.ModelAdmin):
    pass
