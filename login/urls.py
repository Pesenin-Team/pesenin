from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    # path('login/', cas_views.LoginView.as_view(), name='login'),
    # path('logout/', cas_views.LogoutView.as_view(), name='logout'),
]
