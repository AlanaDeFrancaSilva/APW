from rest_framework import serializers
from ..models import Produto
from .marca import MarcaSerializer
from .categoria import CategoriaSerializer

class ProdutoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        
class ProdutoReadSerializer(serializers.ModelSerializer):
    marca_FK = MarcaSerializer(read_only=True) # 3) Facilite o trabalho do frontend, para que no endpoint GET de produtos, seja possível...
    categoria_FK = CategoriaSerializer(read_only=True)
    
    class Meta:
        model = Produto
        fields = '__all__'
        many= True
        





