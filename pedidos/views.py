from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from pedidos.forms import PedidoForm
from .models import Plato, Pedido
import json

# Create your views here.
def home(request):
    return render(request, "base.html")


def menu(request):
    platos = Plato.objects.all()
    return render(request, "pedidos/menu.html", {"platos": platos})
    

def crear_pedido(request):
    if request.method == 'POST':
        try:
            form = PedidoForm(request.POST)
            if form.is_valid():
                pedido = form.save()
                return redirect(listar_pedidos)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        form = PedidoForm()
    return render(request, "pedidos/crear_pedido.html", {"form": form})

    
def listar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-fecha_pedido')
    return render(request, "pedidos/listar_pedidos.html", {"pedidos": pedidos})