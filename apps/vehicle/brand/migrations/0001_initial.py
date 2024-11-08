# Generated by Django 5.1.2 on 2024-11-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название марки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='brand/')),
            ],
            options={
                'verbose_name': 'Марку машины',
                'verbose_name_plural': 'Марки машин',
            },
        ),
    ]
