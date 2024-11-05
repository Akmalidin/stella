from django.db import models

class Reviews(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя клиента')
    img = models.ImageField(upload_to='reviews/', verbose_name='Фото клиента', blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий клиента')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'