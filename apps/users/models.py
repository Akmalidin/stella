# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    profile_img = models.ImageField(upload_to='profile_images/', blank=True, null=True, verbose_name='Фото профиля')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
