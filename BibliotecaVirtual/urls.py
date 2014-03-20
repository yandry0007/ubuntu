from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BibliotecaVirtual.views.home', name='home'),
    # url(r'^BibliotecaVirtual/', include('BibliotecaVirtual.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^' , include('app.hm.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #INICIO
    url(r'^',include('app.inicio.urls')),
    #AUTORES
    url(r'^autor/',include('app.autores.urls')),
    #WEBSERVICES
    url(r'^',include('app.webServices.wsProductos.urls')),
    #VENTAS
    url(r'^',include('app.ventas.urls')),
    #MEDIA
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

    

)
