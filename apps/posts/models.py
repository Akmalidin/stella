from django.db import models
from apps.category.models import Category
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    type_of_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    complete = models.BooleanField(default=False, verbose_name='Завершено')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    region = models.CharField(max_length=255, verbose_name='Регион')
    rooms = models.CharField(max_length=255, verbose_name='Количество комнат')
    area = models.CharField(max_length=255, verbose_name='Площадь')
    floor = models.CharField(max_length=255, verbose_name='Этаж')
    price = models.CharField(max_length=255, verbose_name='Цена в $')
    description = models.TextField(verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    image = models.ImageField(upload_to='posts/', verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", blank=True, null=True)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Изображение поста' 
        verbose_name_plural = 'Изображения постов'    

class CustomerPost(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИМ')
    type_of_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    region = models.CharField(max_length=255, verbose_name='Регион')
    rooms = models.IntegerField(verbose_name='Количество комнат')
    price = models.IntegerField(verbose_name='Цена в $')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Пост клиента'
        verbose_name_plural = 'Постлиста клиентов'
    def __str__(self):
        return self.name