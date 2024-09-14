from django.db import models

# Create your models here.
class Applications(models.Model):
  companyname = models.CharField(max_length=255)
  position = models.CharField(max_length=255)
  date_applied = models.DateField()
  status = models.CharField(max_length=255)

class ChatMessage(models.Model):
  author = models.CharField(max_length=255)
  receiver = models.CharField(max_length=255)
  message = models.CharField(max_length=255)
  timestamp = models.DateTimeField(auto_now_add=True)
  # user = models.CharField(max_length=255)
  # company = models.CharField(max_length=255)