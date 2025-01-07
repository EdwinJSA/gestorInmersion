from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('validarUsuario/', views.validarUsuario, name='validarUsuario'),
    path('home', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
]
