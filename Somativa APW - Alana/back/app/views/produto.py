from rest_framework.viewsets import ModelViewSet
from ..models import Produto
from ..serializers.produto import ProdutoReadSerializer, ProdutoWriteSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..filters.produto_filter import ProdutoFilter 


class ProdutoView(ModelViewSet):
    queryset = Produto.objects.all()
    filterset_class = ProdutoFilter 

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProdutoReadSerializer   # GET → detalhado
        return ProdutoWriteSerializer      # POST/PUT → só IDs
