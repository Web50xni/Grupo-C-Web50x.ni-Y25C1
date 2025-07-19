from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name= 'home'),
    path('menu/', views.menu, name= 'menu'),
    path('pedido/', views.crear_pedido, name='crear_pedido'),
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
]
