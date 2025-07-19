from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu),
    path('pedido/', views.crear_pedido),
    path('pedidos/', views.listar_pedidos),
]
