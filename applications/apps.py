from django.apps import AppConfig


class ApplicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications'
    verbose_name = 'Application'

    def ready(self):
         print(44)
         import applications.signals

