from django.shortcuts import render

# Create your views here.

def antri(request):
    return render(request, 'queue/index.html')
