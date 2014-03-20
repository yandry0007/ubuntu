# Create your views here.
from django.views.generic import CreateView,TemplateView
from .models import Autor
from .models import Invitado
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext

class RegistrarAutor(CreateView):
	template_name = 'autores/registrarAutor.html'
	model = Autor #Vista tipo Autor se cargan todos los atributos de la clase autor 
	success_url = reverse_lazy('registrar_a')
 	
 	def post(self, request, *args, **kwargs):
		estado = False
		autor = Autor()
		autor.nombre = request.POST['nombre']
		autor.pais = request.POST['pais']
		autor.descripcion = request.POST['descripcion']
		autor.foto =request.FILES['foto']
		autor.save()
		estado = True
		dic = {'estado': estado}
		return render_to_response('autores/registrarAutor.html',dic, context_instance=RequestContext(request))


	 
class ReportarAutor(TemplateView):
	template_name = 'autores/reportarAutor.html'





class RegistrarInvitado(CreateView):
	template_name = 'invitado/registrarInvitado.html'
	model = Invitado
	success_url = reverse_lazy('registrar_invitado')

	def post(self, request, *args, **kwargs):
		estado = False
		invitado = Invitado()
		invitado.nombre = request.POST['nombre']
		invitado.pais = request.POST['pais']
		invitado.telefono = request.POST['telefono']
		invitado.foto = request.FILES['foto']
		invitado.save()
		estado = True
		dic = {'estado': estado}
		return render_to_response('invitado/registrarInvitado.html',dic, context_instance=RequestContext(request))



class ReportarInvitado(TemplateView):
	template_name = 'invitado/reportarInvitado.html'

