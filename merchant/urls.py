from django.urls import path
from . import views

app_name = 'merchant'

urlpatterns = [
    path('', views.merchant, name='merchant'),
    path('makanan', views.makanan, name='makanan'),
    path('makanan/<pk>', views.detail_makanan, name='detail')
]
