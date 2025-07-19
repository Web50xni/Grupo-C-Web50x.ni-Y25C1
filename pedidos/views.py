from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Plato, Pedido
import json

# Create your views here.
def menu(request):
    platos = Plato.objects.all()
    texto = "Menu de El Gueguense:\n"

    for plato in platos:
        texto += f"{plato.nombre} - {plato.precio} C$ - {plato.descripcion}\n"

    return HttpResponse(texto, content_type="text/plain")

@csrf_exempt
def crear_pedido(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre_cliente = data['nombre_cliente']
            direccion = data['direccion']
            ids_platos = data['platos']
            pedido = Pedido.objects.create(nombre_cliente=nombre_cliente, direccion=direccion)
            pedido.platos.set(ids_platos)
            
            return JsonResponse({'mensaje': 'Pedido creado exitosamente'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Metodo no permitido'}, status=405)
    
def listar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-fecha_pedido')
    resultado = []

    for pedido in pedidos:
        resultado.append({
            "cliente": pedido.nombre_cliente,
            "direccion": pedido.direccion,
            "fecha_pedido": pedido.fecha_pedido.strftime('%Y-%m-%d %H:%M:%S'),
            "platos": [plato.nombre for plato in pedido.platos.all()],
        })

    return JsonResponse(resultado, safe=False)