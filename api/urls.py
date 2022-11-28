from django.urls import path

from api import views

urlpatterns = [

    path('apicategoria/', views.categoria_list),
    path('apicategoria/<int:id>', views.categoria_detail),

    path('apiusuario/', views.usuario_list),
    path('apiusuario/<int:id>', views.usuario_detail),

    path('apiproducto/', views.producto_list),
    path('apiproducto/<int:id>', views.producto_detail),

    path('apimarca/', views.marca_list),
    path('apimarca/<int:id>', views.marca_detail),

    path('apicarro/', views.carro_list),
    path('apicarro/<int:id>', views.carro_detail),

    path('apisubscripcion/', views.subscripcion_list),
    path('apisubscripcion/<int:id>', views.subscripcion_detail),

]