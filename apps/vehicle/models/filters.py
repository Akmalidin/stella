# vehicle/filters.py
import django_filters
from .models import Vehicle
from apps.vehicle.brand.models import Brand
from apps.vehicle.seller.models import Seller
class VehicleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Название автомобиля')  # Filter by name
    seller = django_filters.ModelChoiceFilter(queryset=Seller.objects.all(), label='Продавец')  # Filter by seller
    brand = django_filters.ModelChoiceFilter(queryset=Brand.objects.all(), label='Марка')  # Filter by brand
    year = django_filters.RangeFilter(label='Год выпуска')  # Filter by year range
    mileage = django_filters.RangeFilter(label='Пробег')  # Filter by mileage range
    engine_capacity = django_filters.RangeFilter(label='Объем двигателя')  # Filter by engine capacity range
    type_of_fuel = django_filters.ChoiceFilter(choices=Vehicle._meta.get_field('type_of_fuel').choices, label='Тип топлива')  # Filter by fuel type
    color = django_filters.CharFilter(lookup_expr='icontains', label='Цвет')  # Filter by color
    state = django_filters.ChoiceFilter(choices=Vehicle._meta.get_field('state').choices, label='Состояние')  # Filter by state (new or used)
    box = django_filters.ChoiceFilter(choices=Vehicle._meta.get_field('box').choices, label='Кузов')  # Filter by body type
    steering_wheel = django_filters.ChoiceFilter(choices=Vehicle._meta.get_field('steering_wheel').choices, label='Руль')  # Filter by steering wheel position
    kuzov = django_filters.CharFilter(lookup_expr='icontains', label='Кузов')  # Filter by body type
    region = django_filters.CharFilter(lookup_expr='icontains', label='Регион')  # Filter by region
    price = django_filters.RangeFilter(label='Цена')  # Filter by price range

    class Meta:
        model = Vehicle
        fields = ['name', 'brand', 'year', 'mileage', 'engine_capacity', 'type_of_fuel', 'color', 
                  'state', 'box', 'steering_wheel', 'kuzov', 'region', 'price', 'created']
