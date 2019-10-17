from django.shortcuts import render
from .models import Merchant

# Create your views here.


def merchant(request):
    
    return render(request, 'merchant/index.html')

def makanan(request):
    return render(request, 'makanan/index.html')
