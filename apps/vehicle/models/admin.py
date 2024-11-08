from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'type_of_fuel', 'region', 'price', 'created')
    search_fields = ('name', 'brand', 'type_of_fuel', 'region', 'price')
    list_filter = ('brand', 'type_of_fuel', 'region', 'price', 'steering_wheel', 'kuzov', 'created', 'state')
    list_per_page = 10

admin.site.register(Vehicle, VehicleAdmin)