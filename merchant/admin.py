from django.contrib import admin
from .models import Merchant
from .models import Makanan

admin.site.register(Merchant)

# Register your models here.

admin.site.register(Makanan)