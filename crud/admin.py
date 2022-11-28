from django.contrib import admin
from .models import Categoria, Marca, Subscripcion, TipoPago, Usuario,Producto,TipoUsuario,Carro


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','rut','dvRut','nUsuario','nombre','apellido','correo','contrasena','direccion','nDireccion','dNac','mNac','aNac']
    list_filter  = ['id','rut']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','codBarra','nombre','precioCosto','precioVenta','marca','categoria','imagen']
    list_filter  = ['id','codBarra','marca','categoria']

class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'activo']
    list_filter  = ['id','nombre', 'activo']

class TipoPagoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'activo']
    list_filter  = ['id','nombre', 'activo']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'activo']
    list_filter  = ['id','nombre', 'activo']

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'activo']
    list_filter  = ['id','nombre', 'activo']

class CarroAdmin(admin.ModelAdmin):
    list_display = ['id','id_usuario','cantidad']
    list_filter  = ['id','id_usuario']


class SubscripcionAdmin(admin.ModelAdmin):
    list_display = ['id','idUsuario','created_at','tipoPago','AporteMensual','nTarjeta','venc','cvv']
    list_filter  = ['id','idUsuario']



# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(TipoPago, TipoPagoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Carro, CarroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subscripcion, SubscripcionAdmin)
