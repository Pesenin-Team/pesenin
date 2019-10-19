from django.urls import path
from . import views

app_name = 'merchant'

urlpatterns = [
    path('', views.merchant, name='merchant'),
    path('makanan', views.makanan, name='makanan'),
    path('makanan/search_makanan', views.search_makanan, name='search_makanan'),
    path('search_merchant', views.search_merchant, name='search_merchant'),
    path('makanan/<int:pk>', views.detail_makanan, name='detail'),
]
