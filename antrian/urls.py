from django.urls import path
from . import views

app_name = 'antrian'
urlpatterns = [
    path('', views.antri, name='queue'),
    path('tambah/<int:pk>', views.tambah_antrian, name='tambah'),
    path('search', views.search_antrian, name='search')
]
