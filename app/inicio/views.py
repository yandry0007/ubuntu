from django.shortcuts import render_to_response
from django.views.generic import TemplateView,FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles


class Registrarse(FormView):
	template_name = 'inicio/registrarse.html' #envio una variable a registrarse y tengo q recogerla ahi
	form_class = UserForm
	success_url = reverse_lazy('registrarsee')

	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario = user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse , self).form_valid(form)


 




# Diferencias entre una vista de Clase y un metodo 
#def index(request):
#	return render_to_response('inicio/index.html')
#class  index2(TemplateView):
#	template_name = 'inicio/index2.html'

