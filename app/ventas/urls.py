from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('app.hm.views',

    url(r'^add/producto/$','add_product_view', name='vista_agregar_producto'),
    url(r'^edit/producto/(?P<id_prod>.*)/$','edit_product_view', name='vista_edit_producto'),
    )