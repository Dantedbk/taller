from . import views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home , name='home'),
    path('catalogo',views.catalogo, name='catalogo'),
    path('agenda',views.agenda, name='agenda'),
    path('producto',views.producto, name='producto'),
    path('venta', views.venta , name='venta'),
    path('registro', views.registro , name='registro'),
    path('registroproducto', views.registroProducto , name='registroproducto'),
    path('registroservicios', views.registroServicios , name='registroservicios'),
    path('carro', views.carro , name='carro'),
    path('perfil', views.perfil , name='perfil'),
    path('logoutUser', views.logoutUser , name='logoutUser'),
    ]
    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

