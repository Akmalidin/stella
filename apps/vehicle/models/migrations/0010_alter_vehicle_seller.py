# Generated by Django 5.1.2 on 2024-11-08 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0009_vehicle_seller'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.seller', verbose_name='Продавец'),
            preserve_default=False,
        ),
    ]
