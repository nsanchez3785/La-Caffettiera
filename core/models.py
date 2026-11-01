from django.db import models

class Politicas(models.Model):
    TIPOS = [
        ('privacidad', 'Política de privacidad'),
        ('cookies', 'Política de cookies'),
        ('legal', 'Aviso legal'),
    ]
    tipo = models.CharField(max_length=20,choices=TIPOS,unique=True,verbose_name='Tipo de política')
    descripcion = models.TextField(verbose_name='Descripción')
    def __str__(self):
        return self.get_tipo_display()
    class Meta:
        db_table = 'politicas'
        verbose_name = 'Política'
        verbose_name_plural = 'Políticas'