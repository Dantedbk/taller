from django.contrib import auth
from django.shortcuts import render,redirect
from django.urls import reverse
from crud.models import Categoria,Producto, Usuario, Marca,Carro
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import math 
import random
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from .models import Event
from django import forms

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

    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)


    contexto = {}

    listado = Producto.objects.all()
    
    if request.method == 'POST':

        if 'btnPedir' in request.POST:
            cantidad = request.POST['txtCantidad']
            
            producto = Producto.objects.get(id=request.POST['btnPedir'])

            if Carro.objects.filter(productos=producto).exists():
                foo = Carro.objects.get(productos=producto)
                foo.cantidad = int(cantidad)
                foo.save()
            else:
                Carro.objects.create(id_usuario = user,productos = producto,cantidad = cantidad, activo = True)

        if 'btnEliminar' in request.POST:
            carro = Carro.objects.get(id = request.POST['txtId'])
            carro.delete()
    listado4 = Carro.objects.all()
    contexto = {'listado': listado,
                'listado4': listado4}


    return render(request, 'catalogo.html', contexto)




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


    listado = Marca.objects.all()
    listado2 = Categoria.objects.all()
    listado3 = Producto.objects.all()

    contexto = {}

    contexto = {'listado': listado,
                'listado2': listado2,
                'listado3': listado3}

    if request.method == 'POST':
        print(request.POST)
        # captura de datos, obtenidos desde el formulario (plantilla)
            
        codBar = random.random()
        nombre = request.POST['txtNombre']
        precioCosto = request.POST['txtprecioCosto']
        precioVenta = request.POST['txtPrecioVenta']
        marca = request.POST['txtMarca']
        categoria = request.POST['txtCategoria']
        descripcion = request.POST['txtDescripcion']
        stock = request.POST['txtStock']

        # producto ----------------------------------------------------------------------------------

        # Marca  ------------------------------------------------------------------------------------

        idMarca      = int("0" + request.POST['txtIdMarca'])
        nombreMarca  = request.POST['txtNombreMarcaEditar']    
        activoMarca = False

        idCategoria      = int("0" + request.POST['txtIdCategoria'])
        nombreCategoria  = request.POST['txtNombreCategoriaEditar']    
        activoCategoria = False

        idProducto = int("0" + request.POST['txtId'])


        if request.POST.get('chkActivoMarca', False):
            activoMarca = True

        if request.POST.get('chkActivoCategoria', False):
            activoCategoria = True

        if len(request.FILES) != 0:
            imagen = request.FILES['imagen']

        if 'btnGuardarp' in request.POST: 
            if idProducto < 1:
                Producto.objects.create( codBarra = codBar, nombre=nombre, precioCosto=precioCosto,stock = stock,
                                        precioVenta=precioVenta, marca=marca,categoria=categoria, descripcion=descripcion,
                                        imagen=imagen)
            else: 
                item = Producto.objects.get(pk = idProducto) # busca 1 elemento que coincida con el pk o id
                item.nombre = nombre
                item.codBarra = codBar
                item.precioCosto=precioCosto
                item.precioVenta=precioVenta
                item.marca=marca
                item.stock = stock
                item.categoria=categoria
                item.descripcion=descripcion
                item.imagen=imagen
                item.save()
    
        elif 'btnGuardarMarca' in request.POST: # detecta si el guardar fue presionado
            if idMarca < 1:
                Marca.objects.create(nombre = nombreMarca, activo = activoMarca)
            else:
                item = Marca.objects.get(pk = idMarca) # busca 1 elemento que coincida con el pk o id
                item.nombre = nombreMarca
                item.activo = activoMarca
                item.save()

        elif 'btnEliminarMarca' in request.POST:
            item = Marca.objects.get(pk = idMarca) # busca 1 elemento que coincida con el pk o id
            item.delete()

        elif 'btnGuardarCategoria' in request.POST: # detecta si el guardar fue presionado
            if idCategoria < 1:
                Categoria.objects.create(nombre = nombreCategoria, activo = activoCategoria)
            else:
                item = Categoria.objects.get(pk = idCategoria) # busca 1 elemento que coincida con el pk o id
                item.nombre = nombreCategoria
                item.activo = activoCategoria
                item.save()

        elif 'btnEliminarCategoria' in request.POST:
            item = Categoria.objects.get(pk = idCategoria) # busca 1 elemento que coincida con el pk o id
            item.delete()

        elif 'btnEliminarProducto' in request.POST:
            item = Producto.objects.get(pk = idProducto) # busca 1 elemento que coincida con el pk o id
            item.delete()

    return render(request, 'registroproducto.html', contexto)





