from django.shortcuts import render, redirect
from .models import Queue
from merchant.models import Makanan
# Create your views here.


def antri(request):
    if (request.user.is_authenticated):
        user = request.user
        queue_list = Queue.objects.filter(user=user)
        content = {
            "antrian": queue_list
        }
        return render(request, 'queue/index.html', content)
    return render(request, 'queue/index.html',)


def tambah_antrian(request, pk):
    if (request.user.is_authenticated):
        user = request.user
        makanan = Makanan.objects.get(pk=pk)
        nama = makanan.nama
        info = "Not Ready"
        link = makanan.foto
        antrian_baru = Queue(
            user=user, nama_makanan=nama, status=info, foto=link)
        antrian_baru.save()
        return redirect('antrian:queue')


def search_antrian(request):
    nama = request.POST.get('search')
    try:
        antrian = Queue.objects.get(nama_makanan=nama)
        return render(request, 'queue/search.html', {'queue': antrian})
    except Queue.DoesNotExist:
        error = "Sorry looks like your food is not here."
        return render(request, 'queue/search.html', {'error': error})
