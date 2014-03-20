from django.http import HttpResponse
from app.ventas.models import producto
#Integramos la serializacion de objetos
from django.core import serializers


def wsProductos_view(request):
	data = serializers.serialize("json", producto.objects.filter(status=True))
	#retorna la info en formato json
	return HttpResponse(data,mimetype='aplication/json')