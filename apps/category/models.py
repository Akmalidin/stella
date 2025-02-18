from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
