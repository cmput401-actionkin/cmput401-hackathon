from django.db import models

# Create your models here.
class Applications(models.Model):
  companyname = models.CharField(max_length=255)
  position = models.CharField(max_length=255)
  date_applied = models.DateField()
  status = models.CharField(max_length=255)