from django.db import models
from django.contrib.auth.models import User

# si definen un modelo nuevo deberan ejecutar makemigrations y migrate
# para que traspase el modelo a la base de datos


# Create your models here.

class Producto(models.Model):
    codBarra = models.IntegerField(db_index=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precioCosto = models.IntegerField()
    precioVenta = models.IntegerField()
    marca = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    stock = models.IntegerField()
    imagen = models.ImageField()

    def __int__(self):
        return self.codBarra
    

class Usuario(models.Model):
    rut = models.CharField(max_length=100,db_index=True)
    dvRut = models.CharField(max_length=100)
    nUsuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    nDireccion = models.CharField(max_length=100)
    dNac = models.CharField(max_length=100)
    mNac = models.CharField(max_length=100)
    aNac = models.CharField(max_length=100)

    def __str__(self):
        return self.rut

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField()
    
    def __str__(self):
        return self.nombre

class Subscripcion(models.Model):
    idUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tipoPago = models.ForeignKey('TipoPago', on_delete=models.CASCADE)
    AporteMensual = models.CharField(max_length=100)
    nTarjeta = models.CharField(max_length=16)
    venc = models.CharField(max_length=20)
    cvv = models.CharField(max_length=3)



class TipoPago(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField()
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField()

    def __str__(self):
        return str(self.nombre)

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField()

    def __str__(self):
        return str(self.nombre)




class Carro(models.Model):
    id_usuario = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    activo = models.BooleanField(default=None, blank=True, null=True)
    cantidad = models.IntegerField(null=True)
    productos = models.OneToOneField(Producto,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.id_usuario)

