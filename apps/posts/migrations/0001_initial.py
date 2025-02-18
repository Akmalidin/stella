# Generated by Django 5.1.2 on 2024-11-02 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИМ')),
                ('region', models.CharField(max_length=255, verbose_name='Регион')),
                ('rooms', models.IntegerField(verbose_name='Количество комнат')),
                ('price', models.IntegerField(verbose_name='Цена в $')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('type_of_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост клиента',
                'verbose_name_plural': 'Постлиста клиентов',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='posts/', verbose_name='Изображение')),
                ('complete', models.BooleanField(default=False, verbose_name='Завершено')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('region', models.CharField(max_length=255, verbose_name='Регион')),
                ('rooms', models.CharField(max_length=255, verbose_name='Количество комнат')),
                ('area', models.CharField(max_length=255, verbose_name='Площадь')),
                ('floor', models.CharField(max_length=255, verbose_name='Этаж')),
                ('price', models.CharField(max_length=255, verbose_name='Цена в $')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('type_of_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
