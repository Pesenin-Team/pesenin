from django.contrib import admin
from .models import Merchant
from .models import Makanan

# Register your models here.

admin.site.register(Merchant)
admin.site.register(Makanan)