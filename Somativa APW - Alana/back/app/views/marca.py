from rest_framework.viewsets import ModelViewSet
from ..models import Marca
from ..serializers.marca import MarcaSerializer

class MarcaView(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer