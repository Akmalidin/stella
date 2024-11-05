from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.name