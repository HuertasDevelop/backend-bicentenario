from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify


class Areas(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    photo = CloudinaryField('icono', overwrite=True,
                            format="webp", blank=True, null=True)

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Benefits(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Project(models.Model):

    class Coin(models.TextChoices):
        PEN = 'PEN'
        USD = 'USD'
    name = models.CharField(max_length=50, verbose_name='Nombre')
    slug = models.SlugField(max_length=255, null=True,
                            blank=True, unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Descripción')

    place = models.CharField(max_length=100, verbose_name='Lugar')
    from_price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name='precio desde')
    price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name='precio')
    from_area = models.IntegerField(
        blank=True, null=True, verbose_name='Area desde')
    type_coin = models.CharField(
        max_length=5, choices=Coin.choices, default=Coin.PEN, verbose_name='Moneda')

    people_card = CloudinaryField(
        'foto_persona_miniatura', overwrite=True, format="webp", blank=True, null=True)
    banner_card = CloudinaryField(
        'foto_fondo_miniatura', overwrite=True, format="webp", blank=True, null=True)

    slogan = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Slogan')
    banner_detail = CloudinaryField(
        'foto_banner_detalle', overwrite=True, format="webp", blank=True, null=True)

    banner = CloudinaryField(
        'banner_principal', overwrite=True, format="webp", blank=True, null=True)
    link_banner_video = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Link video banner')
    location = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Ubicación')
    ref_location = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Referencia de ubicación')
    areas = models.ManyToManyField(Areas)

    photo_map = CloudinaryField(
        'foto_mapa', overwrite=True, format="webp", blank=True, null=True)
    link_google_maps = models.URLField(
        blank=True, null=True, verbose_name='Link Google Maps')
    link_waze = models.URLField(
        blank=True, null=True, verbose_name='Link Waze')

    photo_feature = CloudinaryField(
        'foto_banner_secundario', overwrite=True, format="webp", blank=True, null=True)

    benefits = models.ManyToManyField(Benefits, verbose_name='Beneficios')

    def save(self, *args, **kwargs):
        if not self.slug:
            to_assign = slugify(self.name)
            if Project.objects.filter(slug=to_assign).exists():
                to_assign = f"{to_assign}-{Project.objects.count()}"
            self.slug = to_assign
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='gallery')
    photo = CloudinaryField('foto', overwrite=True,
                            format="webp", blank=True, null=True)
    alt = models.CharField(max_length=100, blank=True,
                           null=True, verbose_name='Texto alternativo')

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
        ordering = ('-project',)

    def __str__(self):
        return self.project.name
