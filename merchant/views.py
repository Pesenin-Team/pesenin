from django.shortcuts import render, redirect
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
    # merchant = Merchant.objects.get(pk=pk)
    list_makanan = Makanan.objects.all()
    content = {
        "food": list_makanan
    }
    return render(request, 'makanan/index.html', content)


def detail_makanan(request, pk):
    food_details = Makanan.objects.get(pk=pk)
    content = {
        "food_detail": food_details
    }
    return render(request, 'makanan/display.html', content)
