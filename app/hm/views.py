from django.shortcuts import render_to_response
from django.template import RequestContext
from app.ventas.models import producto
from app.hm.forms import ContactForm, LoginForm
from django.core.mail import EmailMultiAlternatives # Enviamos HTML

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

from app.ventas.forms import addProductForm
from django.http import HttpResponseRedirect

#PAGINACION
from django.core.paginator import Paginator,EmptyPage,InvalidPage


def index_view(request):
	return render_to_response('ventas/index.html', context_instance=RequestContext(request))
	
def about_view(request):
	mensaje = "Este es un msj desde la vista"
	ctx = {'msg':mensaje}
	return render_to_response('ventas/about.html',ctx, context_instance=RequestContext(request))

def productos_view(request,pagina):
	lista_prod = producto.objects.filter(status=True) #Algo asi como select * from productos where status=True
	paginator = Paginator(lista_prod,4) #Cuantos elementos quieres por pagina = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)

	ctx = {'productos':productos}
	return render_to_response('ventas/productos.html', ctx, context_instance=RequestContext(request))

def singleProduct_view(request,id_prod):
	prod = producto.objects.get(id=id_prod)
	ctx = {'producto':prod}
	return render_to_response('ventas/SingleProducto.html',ctx,context_instance=RequestContext(request))



def contacto_view(request):
	info_enviado = False #definir si se envio la info
	
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

	else:

		formulario = ContactForm()
	ctx = {'form':formulario, 'email':email, 'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado }
	return render_to_response('ventas/contacto.html', ctx, context_instance=RequestContext(request))


def add_product_view(request):
	info = "Inicializando"
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProductForm(request.POST)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				p = producto()
				p.nombre = nombre
				p.descripcion = descripcion
				p.status = True
				p.save()
				info = "se ha guardado satisfactoriamente"
 			else:
 				info = "informacion con datos incorrecto"
 		form =addProductForm()
 		ctx ={'form':form, 'informacion':info}	
 		return render_to_response('ventas/addProducto.html',ctx, context_instance=RequestContext(request))	
 	else:
 		return HttpResponseRedirect('/index/')



def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')
	else:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/index/')
				else:
					mensaje = "usuario y/o password incorrectos"
		form = LoginForm()
		ctx = {'form':form,'mensaje': mensaje}
		return render_to_response('hm/login.html' ,ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/index/')

def edit_product_view(request,id_prod):
	p = producto.objects.get(id=id_prod)
	if request.method == 'POST':
		form = addProductForm(request.POST,request.FILES)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			p.nombre = nombre
			p.descripcion = descripcion
			#if imagen: #verifica q la imagen sea correcta
				#p.imagen = imagen
			p.save() #guardamos la info editada
			return  HttpResponseRedirect('/producto/%s'%p.id)


	if request.method == "GET":
		form = addProductForm(initial={
					'nombre':p.nombre,
					'descripcion':p.descripcion,

			})
	ctx = {'form':form, 'producto':p}
	return render_to_response('ventas/editProducto.html',ctx,context_instance=RequestContext(request))




# Ver tutoril 15 para completar los 3 campos, imagen precio stock;

#http://www.youtube.com/watch?v=c0CNWF5Oo70

