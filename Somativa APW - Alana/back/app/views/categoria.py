from rest_framework.viewsets import ModelViewSet
from ..models import Categoria
from ..serializers.categoria import CategoriaSerializer

class CategoriaView(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer