from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('app.webServices.wsProductos.views',
    url(r'^ws/productos/$' , 'wsProductos_view', name='ws_productos_url'), #especificar el nombre del metodo de la vista creada
    ) 