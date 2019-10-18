from django.shortcuts import render
from .models import Queue
# Create your views here.


def antri(request):
    if (request.user.is_authenticated):
        user = request.user
        # makanan = "Ayam mentega"
        # info = "Not Ready"
        # link = "../../../static/queue/img/ayam-mentega.jpg"
        # antrian_baru = Queue(
        #     user=user, nama_makanan=makanan, status=info, foto=link)
        # antrian_baru.save()
        queue_list = Queue.objects.filter(user=user)
        content = {
            "antrian": queue_list
        }
        return render(request, 'queue/index.html', content)
    return render(request, 'queue/index.html',)
