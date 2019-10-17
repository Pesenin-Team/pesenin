from django.shortcuts import render

# Create your views here.


def merchant(request):
    merchant = Merchant.objects.all()

    content = [
        "nama": merchant.name
    ]
    return render(request, 'merchant/index.html', content)
