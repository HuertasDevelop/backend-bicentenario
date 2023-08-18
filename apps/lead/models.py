from django.db import models


class Lead(models.Model):
    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
    name = models.CharField(max_length=100, verbose_name='Nombre')
    lastname = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField(max_length=100, verbose_name='Correo')
    type_doc = models.CharField(
        max_length=100, verbose_name='Tipo de documento')
    doc = models.CharField(max_length=100, verbose_name='Documento')
    phone = models.CharField(max_length=100, verbose_name='Telefono')
    message = models.TextField(verbose_name='Mensaje')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    project = models.CharField(
        max_length=100, verbose_name='Proyecto', null=True, blank=True
    )

    def __str__(self):
        return self.name
