from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название марки')
    image = models.ImageField(upload_to='brand/', blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Марку машины'
        verbose_name_plural = 'Марки машин'