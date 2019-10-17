from django.db import models

# Create your models here.
class makanan(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=50)
    foto = models.CharField()

    def __str__(self):
        return self.nama