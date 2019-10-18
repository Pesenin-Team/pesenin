from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Queue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_makanan = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    foto = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_makanan
