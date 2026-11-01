from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    class Meta:
        ordering = ['-created']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'category'
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    published = models.BooleanField(default=True, verbose_name='Fecha de Publicación')
    image = models.ImageField(upload_to='blog', verbose_name='Imagen', null=True, blank=True)
    content = models.TextField(verbose_name='Contenido')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    categories = models.ManyToManyField(Category, verbose_name='Categorías')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    class Meta:
        ordering = ['-created']
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        db_table = 'post'

    def __str__(self):
        return self.title

