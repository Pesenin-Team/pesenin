from django.urls import path
from . import views

app_name = 'antrian'
urlpatterns = [
    path('', views.antri, name='queue')
]
