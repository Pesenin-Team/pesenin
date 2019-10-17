from django.urls import path
from . import views

app_name = 'merchant'

urlpatterns = [
    path('', views.merchant, name='merchant'),
]
