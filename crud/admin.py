from django.contrib import admin
from .models import Categoria, Marca, Subscripcion, TipoPago, Usuario,Producto,TipoUsuario,Carro,Documento,detalleDocumento


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','rut','dvRut','nUsuario','nombre','apellido','correo','contrasena','direccion','nDireccion','dNac','mNac','aNac']
    list_filter  = ['id','rut']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','precioCosto','precioVenta','categoria','imagen']
    list_filter  = ['id']

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

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['nDocumento','tipo','fecha']
    list_filter = ['nDocumento']



class detalleDocumentoAdmin(admin.ModelAdmin):
    list_display = ['id','id_usuario','nDocumento','id_cliente','cantidad','producto']
    list_filter = ['nDocumento']


    
# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(TipoPago, TipoPagoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Carro, CarroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subscripcion, SubscripcionAdmin)
admin.site.register(Documento,DocumentoAdmin)
admin.site.register(detalleDocumento,detalleDocumentoAdmin)
