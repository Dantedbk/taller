from rest_framework import serializers
from crud.models import Categoria, Producto, Subscripcion,Usuario,Marca,Carro

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Categoria
        fields  = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Producto
        fields  = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Usuario
        fields  = "__all__"

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Marca
        fields  = "__all__"

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Carro
        fields  = "__all__"

class SubscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Subscripcion
        fields  = "__all__"
