from django.contrib import auth
from django.shortcuts import render,redirect
from django.urls import reverse
from crud.models import Categoria,Producto, Usuario, Marca,Carro,Servicio
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import math 
import random

listadoProd = Producto.objects.all()


def logoutUser(request):
    Carro.objects.all().delete()
    logout(request)
    return redirect(home)



def perfil(request):
    return render(request,'perfil.html',{})

def agenda(request):
    
    return render(request,'agenda.html',{})



def home(request):
    contexto = {}
    if request.method == 'POST':
        nUsuario = request.POST['txtUsuario']
        contrasena =  request.POST['txtContrasena']

        if 'btnGuardar' in request.POST:
            user = authenticate(request, username=nUsuario, password=contrasena)

            if user is not None:
                login(request, user)
                return render(request, 'home.html', {})

            else:
                pass # Return an 'invalid login' error message.


    return render(request, 'home.html', {})







def carro(request):

    listado = Producto.objects.all()
    listado2 = Usuario.objects.all()
    listado3 = Servicio.objects.all()
    contexto = {}

    contexto = {'listado': listado}

    if request.method == 'POST':

        if 'btnPedir' in request.POST:
            cantidad = request.POST['txtCantidad']
            
            producto = Producto.objects.get(id=request.POST['btnPedir'])

            if Carro.objects.filter(productos=producto).exists():
                foo = Carro.objects.get(productos=producto)
                foo.cantidad = int(cantidad)
                foo.save()
            # else:
            #     Carro.objects.create(id_usuario = user,productos = producto,cantidad = cantidad, activo = True)

        if 'btnEliminar' in request.POST:
            carro = Carro.objects.get(id = request.POST['txtId'])
            carro.delete()
    listado4 = Carro.objects.all()
    contexto = {'listado': listadoProd}



    return render(request, 'carro.html', contexto)









def catalogo(request):


    contexto = {}

    listado = Servicio.objects.all()
    

    contexto = {'listado': listado}


    return render(request, 'catalogo.html', contexto)




def registroServicios(request):


    listado = Producto.objects.all()
    listado2 = Servicio.objects.all()

    contexto = {}

    contexto = {'listado': listado,
                'listado2': listado2}

    if request.method == 'POST':
        print(request.POST)

        # producto ----------------------------------------------------------------------------------
        idProducto = request.POST['txtIdProducto']
        nombreProducto = request.POST['txtNombreProducto']
        precioCosto = request.POST['txtprecioCostoProducto']
        precioVenta = request.POST['txtPrecioVentaProducto']
        stock = request.POST['txtStock']
        categoria = request.POST['txtCategoria']
        descripcion = request.POST['txtDescripcionProducto']

        # producto ----------------------------------------------------------------------------------

        # servicio  ------------------------------------------------------------------------------------

        idServicio      = int("0" + request.POST['txtIdServicio'])
        nombreServicio  = request.POST['txtNombreServicio']
        precioBaseServicio  = request.POST['txtprecioBaseServicio']
        DescripcionServicio  = request.POST['txtDescripcionServicio']

        idServicio = int("0" + request.POST['txtIdServicio'])
        idProducto = int("0" + request.POST['txtIdProducto'])


        if len(request.FILES) != 0:
            imagen = request.FILES['imagenServicio']

        if 'btnGuardarp' in request.POST: 
            if idProducto < 1:
                Producto.objects.create(nombre=nombreProducto, 
                                        precioCosto=precioCosto,
                                        stock = stock,
                                        precioVenta=precioVenta,
                                        categoria=categoria, 
                                        descripcion=descripcion)
            else: 
                item = Producto.objects.get(pk = idProducto) # busca 1 elemento que coincida con el pk o id
                item.nombreProducto = nombreProducto
                item.precioCosto=precioCosto
                item.precioVenta=precioVenta
                item.stock = stock
                item.categoria=categoria
                item.descripcion=descripcion
                item.save()
    
        elif 'btnGuardarServicio' in request.POST: # detecta si el guardar fue presionado
            if idServicio < 1:
                Servicio.objects.create(nombre = nombreServicio,
                                        valor = precioBaseServicio,
                                        descripcion = DescripcionServicio,
                                        imagen = imagen)
            else:
                item = Servicio.objects.get(pk = idServicio) # busca 1 elemento que coincida con el pk o id
                item.nombreServicio = nombreServicio,
                item.precioBaseServicio = precioBaseServicio,
                item.DescripcionServicio = DescripcionServicio,
                item.imagen = imagen,
                item.save()

        elif 'btnEliminarServicio' in request.POST:
            item = Servicio.objects.get(pk = idServicio) # busca 1 elemento que coincida con el pk o id
            item.delete()

        elif 'btnEliminarProducto' in request.POST:
            item = Producto.objects.get(pk = idProducto) # busca 1 elemento que coincida con el pk o id
            item.delete()




    return render(request, 'registroservicios.html',{})


def producto(request):
    return render(request, 'producto.html', {})


def venta(request):
    return render(request, 'home.html')


def registro(request):

    contexto = {}
    listado = Usuario.objects.all()

    if request.method == 'POST':

        idUsuario = request.POST['txtId']
        rut = request.POST['txtRut']
        dv = request.POST['txtDV']
        nusuario = request.POST['txtnUsuario']
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        correo = request.POST['txtCorreo']
        contrasena = request.POST['txtContrasenna']
        contrasena2 = request.POST['txtContrasenna2']
        direccion = request.POST['txtDireccion']
        nDireccion = request.POST['txtNDireccion']
        dNac = request.POST['txtDia']
        mNac = request.POST['txtMes']
        aNac = request.POST['txtAnno']

        serie = 2
        suma = 0

        for i in reversed(rut):
            suma += int(i)*serie
            print(int(i)*serie)
            if serie == 7:
                serie = 1
            serie += 1
        dvchk = 11 - (suma - math.trunc(suma/11)*11)

        if dvchk == 11:
            dvchk = 0
        elif dvchk == 10:
            dvchk = 'k'

        print(request.POST)
        if 'btnGuardar' in request.POST:
            if not rut or not nombre or not apellido or not correo or not direccion or not nDireccion or not dNac or not mNac or not aNac \
                    or contrasena != contrasena2 or dvchk != dv.lower():

                if idUsuario:
                    Usuario.objects.create(rut=rut,dvRut = dv, nUsuario = nusuario, nombre=nombre, apellido=apellido, correo=correo, contrasena=contrasena,
                                        direccion=direccion, nDireccion=nDireccion, dNac=dNac, mNac=mNac, aNac=aNac)
                    user = User.objects.create_user(username=nusuario, email=correo, password=contrasena)

                    user.save()
                else:
                    usuario = Usuario.objects.get(id = idUsuario)
                    usuario.rut = rut
                    usuario.dvRut = dv 
                    usuario.nUsuario = nusuario 
                    usuario.nombre = nombre 
                    usuario.apellido = apellido 
                    usuario.correo = correo 
                    usuario.contrasena = contrasena 
                    usuario.direccion = direccion 
                    usuario.dNac = aNac 
                    usuario.mNac = aNac 
                    usuario.aNac = aNac 
                    usuario.save()
        if 'btnEliminar' in request.POST:
            usuario = Usuario.objects.get(id = idUsuario)
            usuario.delete()


    contexto = {'listado':listado}


    return render(request, 'registro.html',contexto)


def registroProducto(request):

    return render(request, 'registroproducto.html')







