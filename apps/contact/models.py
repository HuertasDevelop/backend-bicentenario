from django.db import models
from cloudinary.models import CloudinaryField


class ContactEnterprice(models.Model):

    banner_top = CloudinaryField(
        'banner_superior', overwrite=True, format="webp", blank=True, null=True)
    banner_bot = CloudinaryField(
        'banner_inferior', overwrite=True, format="webp", blank=True, null=True)
    people_photo = CloudinaryField(
        'foto_persona', overwrite=True, format="webp", blank=True, null=True)
    photo_number_phone = CloudinaryField(
        'foto_numero_telefono', overwrite=True, format="webp", blank=True, null=True)
    number_phone = models.CharField(
        max_length=100, verbose_name='Número de teléfono')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.number_phone

    def save(self, *args, **kwargs):
        # ver error 500
        try:
            print('try')
        except:
            print('except')
        super(ContactEnterprice, self).save(*args, **kwargs)
