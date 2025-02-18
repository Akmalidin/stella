# Generated by Django 5.1.2 on 2024-11-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_vehicle_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='box',
            field=models.CharField(choices=[('Механика', 'Механика'), ('Автомат', 'Автомат')], max_length=10, verbose_name='Кузов'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название автомобиля'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='state',
            field=models.CharField(choices=[('Новый', 'Новый'), ('БУ', 'Б/у')], max_length=10, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='steering_wheel',
            field=models.CharField(choices=[('Левый', 'Левый'), ('Правый', 'Правый')], max_length=10, verbose_name='Руль'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type_of_fuel',
            field=models.CharField(choices=[('Бензин', 'Бензин'), ('Дизель', 'Дизель'), ('Электрика', 'Электрика')], max_length=10, verbose_name='Тип топлива'),
        ),
    ]
