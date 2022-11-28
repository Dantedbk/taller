from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from crud.models import Carro, Categoria, Marca, Producto, Subscripcion, Usuario
from api.serializers import CarroSerializer, CategoriaSerializer, MarcaSerializer, ProductoSerializer, SubscripcionSerializer, UsuarioSerializer

# Create your views here.
@api_view(['GET','POST'])
def categoria_list(request, format=None):

    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)




#########################################################categoria

@api_view(['GET','PUT','DELETE'])
def categoria_detail(request,id, format=None):

    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categoria.delete()
        return (Response(status=status.HTTP_204_NO_CONTENT))


################################################################# marca



@api_view(['GET','POST'])
def marca_list(request, format=None):

    if request.method == 'GET':
        marcas = Marca.objects.all()
        serializer = MarcaSerializer(marcas, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET','PUT','DELETE'])
def marca_detail(request,id, format=None):

    try:
        marcas = Marca.objects.get(pk=id)
    except Marca.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MarcaSerializer(marcas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MarcaSerializer(marcas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        marcas.delete()
        return (Response(status=status.HTTP_204_NO_CONTENT))




###########################################################################################


@api_view(['GET','POST'])
def producto_list(request, format=None):

    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET','PUT','DELETE'])
def producto_detail(request,id, format=None):

    try:
        productos = Producto.objects.get(pk=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductoSerializer(productos)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductoSerializer(productos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        productos.delete()
        return (Response(status=status.HTTP_204_NO_CONTENT))



@api_view(['GET','POST'])
def usuario_list(request, format=None):

    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET','PUT','DELETE'])
def usuario_detail(request,id, format=None):

    try:
        usuarios = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuarios)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuarios.delete()
        return (Response(status=status.HTTP_204_NO_CONTENT))


@api_view(['GET','POST'])
def carro_list(request, format=None):

    if request.method == 'GET':
        carro = Carro.objects.all()
        serializer = CarroSerializer(carro, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)






@api_view(['GET','PUT','DELETE'])
def subscripcion_detail(request,id, format=None):

    try:
        subscripcion = Subscripcion.objects.get(pk=id)
    except Subscripcion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubscripcionSerializer(subscripcion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubscripcionSerializer(subscripcion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subscripcion.delete()
        return (Response(status=status.HTTP_204_NO_CONTENT))



@api_view(['GET','POST'])
def subscripcion_list(request, format=None):

    if request.method == 'GET':
        subscripcion = Subscripcion.objects.all()
        serializer = SubscripcionSerializer(subscripcion, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SubscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])
def carro_detail(request,id, format=None):

    try:
        carro = Carro.objects.get(pk=id)
    except Carro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarroSerializer(carro)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarroSerializer(carro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        carro.delete()
        return (Response(status=status.HTTP_204_NO_CONTENT))



