from rest_framework.routers import DefaultRouter
from .views.produto import ProdutoView
from .views.setor import SetorView
from .views.marca import MarcaView
from .views.escaninhos import EscaninhosView
from .views.categoria import CategoriaView
from .views.custom_user import CustomUserView
#from .views import *

router = DefaultRouter()
router.register(r'produtos',ProdutoView)
router.register(r'setor',SetorView)
router.register(r'marca',MarcaView)
router.register(r'escaninhos',EscaninhosView)
router.register(r'categoria',CategoriaView)
router.register(r'custom-user',CustomUserView)

urlpatterns = router.urls