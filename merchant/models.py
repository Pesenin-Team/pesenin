from django.db import models

# Create your models here.
class Merchant(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    linkgambar = models.CharField(max_length=200)


