from rest_framework.viewsets import ModelViewSet
from ..models import CustomUser
from ..serializers.custom_user import CustomUserSerializer


class CustomUserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
