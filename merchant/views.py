<<<<<<< HEAD
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
=======
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

def detail_makanan(request, pk):
    food_details = Makanan.objects.get(pk=pk)
    content = {
        "food_detail": food_details
    }
    return render(request, 'makanan/display.html', content)
>>>>>>> 32675d90c28c6b0a5b1b74fb134887c63da8e15b
