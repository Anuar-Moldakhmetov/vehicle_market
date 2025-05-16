from django.contrib import admin
from .models import Aviation
from .models import ArmoredVehicles

@admin.register(Aviation)
class AviationAdmin(admin.ModelAdmin):
    ...

@admin.register(ArmoredVehicles)
class ArmoredVehiclesAdmin(admin.ModelAdmin):
    ...
# Register your models here.
