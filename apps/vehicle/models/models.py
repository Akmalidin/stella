from django.db import models
from apps.vehicle.brand.models import Brand
from apps.vehicle.seller.models import Seller
class Vehicle(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название автомобиля')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Продавец')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Марка')
    year = models.IntegerField(verbose_name='Год выпуска')
    mileage = models.IntegerField(verbose_name='Пробег')
    engine_capacity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Объем двигателя')
    type_of_fuel = models.CharField(max_length=10, choices=[('Бензин', 'Бензин'), ('Дизель', 'Дизель'), ('Электрика', 'Электрика')], verbose_name='Тип топлива')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    state = models.CharField(max_length=10, choices=[('Новый', 'Новый'), ('БУ', 'Б/у')], verbose_name='Состояние')
    box = models.CharField(max_length=10, choices=[('Механика', 'Механика'), ('Автомат', 'Автомат')], verbose_name='Кузов')
    steering_wheel = models.CharField(max_length=10, choices=[('Левый', 'Левый'), ('Правый', 'Правый')], verbose_name='Руль')
    kuzov = models.CharField(max_length=100, verbose_name='Кузов')
    region = models.CharField(max_length=100, verbose_name='Регион')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicle/images/', verbose_name='Изображение')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки", blank=True, null=True)
    def __str__(self):
        return f"Image for {self.vehicle.name}"
