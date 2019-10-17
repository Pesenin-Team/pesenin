from django.shortcuts import render

# Create your views here.


def merchant(request):
    return render(request, 'merchant/index.html')

def makanan(request):
    list_makanan = makanan.objects.all()
    return render(request, 'makanan/index.html')