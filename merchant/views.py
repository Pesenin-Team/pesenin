from django.shortcuts import render
from .models import Merchant

# Create your views here.


def merchant(request):
    nama_merchant = "Warkop DKI"
    decs = "Sedia Mie Instant, Jeroan, dan Kopi"
    link_gambar = "../../static/merchant/img/"
    return render(request, 'merchant/index.html')


