from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.projects'
    vars = {
        'verbose_name': 'Proyecto',
        'verbose_name_plural': 'Proyectos',
    }
