from django.db import models
from cloudinary.models import CloudinaryField


class HomePage(models.Model):
    class Type(models.TextChoices):
        BANNER_1 = 'BANNER_1'
        BANNER_2 = 'BANNER_2'
        BANNER_3 = 'BANNER_3'
        FORM = 'FORM'

    description = models.TextField(verbose_name='Descripción')
    link = models.URLField(max_length=200, blank=True,
                           null=True, verbose_name='Link')
    photo = CloudinaryField(
        'foto', overwrite=True, format="webp", blank=True, null=True)
    type = models.CharField(
        max_length=20, choices=Type.choices, unique=True, verbose_name='Tipo')

    class Meta:
        verbose_name = 'Pagina de Inicio'
        verbose_name_plural = 'Paginas de Inicio'

    def __str__(self):
        return self.link


class Carousel(models.Model):
    description = models.TextField(verbose_name='Descripción')
    link = models.URLField(max_length=200, blank=True,
                           null=True, verbose_name='Link')
    photo = CloudinaryField(
        'foto', overwrite=True, format="webp", blank=True, null=True)
    active = models.BooleanField(default=False, verbose_name='Activo')
    order = models.IntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'
        ordering = ['order']

    def __str__(self):
        return self.link


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    comment = models.TextField(verbose_name='Comentario')
    photo = CloudinaryField(
        'foto', overwrite=True, format="webp", blank=True, null=True)
    active = models.BooleanField(default=False, verbose_name='Activo')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProjectPage(models.Model):
    class Type(models.TextChoices):
        BANNER_1 = 'BANNER_1'
        BANNER_2 = 'BANNER_2'
        FORM = 'FORM'
    description = models.TextField(verbose_name='Descripción')
    link = models.URLField(max_length=200, blank=True,
                           null=True, verbose_name='Link')
    photo = CloudinaryField(
        'foto', overwrite=True, format="webp", blank=True, null=True)
    type = models.CharField(
        max_length=20, choices=Type.choices, unique=True, verbose_name='Tipo')

    class Meta:
        verbose_name = 'Pagina de Proyectos'
        verbose_name_plural = 'Paginas de Proyectos'

    def __str__(self):
        return self.link
