from rest_framework import serializers
from ..models import Escaninhos
from ..serializers.produto import ProdutoReadSerializer  
from ..models import Produto

class EscaninhosSerializer(serializers.ModelSerializer):
    # Exibir todos os produtos associados ao escaninho
    produtos = ProdutoReadSerializer(source='produto_FK_set', read_only=True, many=True)  # 'produto_FK_set' é a relação reversa entre Produto e Escaninho
    
    class Meta:
        model = Escaninhos
        fields = '__all__'
        many= True