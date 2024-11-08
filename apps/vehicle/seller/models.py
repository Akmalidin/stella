from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    img = models.ImageField(upload_to='seller/', verbose_name='Фото профиля', blank=True, null=True)
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')

    def __str__(self):
        return self.name