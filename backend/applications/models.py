from django.db import models

# Create your models here.
class Applications(models.Model):
  class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
  companyname = models.CharField(max_length=255)
  position = models.CharField(max_length=255)
  date_applied = models.DateField()
  status = models.CharField(max_length=255)


