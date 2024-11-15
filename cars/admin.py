from django.contrib import admin
from .models import Car, CarImage

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'uploaded_at')
