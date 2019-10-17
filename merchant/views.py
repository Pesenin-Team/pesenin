from django.shortcuts import render
from .models import Merchant
from .models import Makanan

# Create your views here.


def merchant(request):
    list_merchant = Merchant.objects.all()
    content = {
        "penjual": list_merchant
    }
    return render(request, 'merchant/index.html', content)

def makanan(request):
    list_makanan = Makanan.objects.all()
    content = {
        "food": list_makanan
    }
    return render(request, 'makanan/index.html', content)