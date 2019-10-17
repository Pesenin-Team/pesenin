from django.db import models
# from dajngo.contrib.auth.models import User

# Create your models here.
class Merchant(models.Model):
    nama_merchant = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    link_gambar = models.CharField(max_length=200)

    def __str__(self):
        return self.nama_merchant

