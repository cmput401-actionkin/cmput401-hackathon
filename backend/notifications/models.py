from django.db import models

class Notifications(models.Model):
  class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
  companyname = models.CharField(max_length=255)
  position = models.CharField(max_length=255)
  date_applied = models.DateField()
  status = models.CharField(max_length=255)
  message = models.CharField(max_length=255)