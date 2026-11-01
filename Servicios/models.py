from django.db import models


# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Título')
    subtitle = models.CharField(max_length = 200, verbose_name = 'Subtítulo')
    image = models.ImageField(upload_to = 'images/')
    content = models.TextField(verbose_name = 'Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    class Meta:
        ordering = ['-created']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        db_table = 'services'

    def __str__(self):
        return self.title

