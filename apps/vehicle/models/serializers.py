from rest_framework import serializers
from .models import Vehicle, VehicleImage

class VehicleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleImage
        fields = ['id', 'image', 'uploaded_at']

class VehicleSerializer(serializers.ModelSerializer):
    images = VehicleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'seller', 'brand', 'year', 'mileage', 'engine_capacity', 'type_of_fuel', 
                  'color', 'state', 'box', 'steering_wheel', 'kuzov', 'region', 'price', 'description', 'created', 'images']

class VehicleImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleImage
        fields = ['vehicle', 'image']