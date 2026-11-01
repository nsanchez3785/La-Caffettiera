from django.db import models

# Create your models here.
class RedesSociales(models.Model):
    REDES = [
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('linkedin', 'LinkedIn'),
    ]
    nombre = models.CharField(max_length=20,choices=REDES,verbose_name='Red Social',default='instagram')
    url = models.URLField(verbose_name='URL')

    def __str__(self):
        return self.get_nombre_display()

    class Meta:
        db_table = 'Redes_Sociales'
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'