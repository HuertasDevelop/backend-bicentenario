from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    class Meta:
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'

    description = models.TextField(verbose_name='Descripción')
    banner_bg = CloudinaryField(
        'banner_fondo', overwrite=True, format="webp", blank=True, null=True)
    banner_info = CloudinaryField(
        'banner_info', overwrite=True, format="webp", blank=True, null=True)

    def __str__(self):
        return self.description


class Stats(models.Model):
    class Meta:
        verbose_name = 'Estadística'
        verbose_name_plural = 'Estadísticas'

    title = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return self.title


class Office(models.Model):
    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    address = models.CharField(max_length=100, verbose_name='Dirección')
    reference = models.CharField(max_length=100, verbose_name='Referencia')
    link_google_maps = models.URLField(
        max_length=200, blank=True, null=True, verbose_name='Link Google Maps')
    link_waze = models.URLField(
        max_length=200, blank=True, null=True, verbose_name='Link Waze')

    def __str__(self):
        return self.address
