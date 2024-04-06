from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

#View set serve para rotear todas as requisições para a função apropriada, ao invés de fazer isso manualmente
# O viewset é genérico e faz o CRUD completo
# Utilizar uma listModelMixin ou GenericAPIView para fazer o CRUD manualmente, permite funções mais específicas

class ProductViewSet(viewsets.ModelViewSet):

    """
    ViewSet --> route every request to the appropriate function

    get -> list -> queryset
    get -> retrieve -> Product instance detail view
    post -> create -> New instance
    put -> update -> Update instance
    patch -> partial_update -> Partial update instance
    delete -> destroy -> Delete instance

    
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lockup_field = 'pk' #default


#viewSet --> serve para rotear todas as requisições para a função apropriada

class ProductGenericView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lockup_field = 'pk' #default

product_list_view = ProductGenericView.as_view({'get': 'list'})
product_list_detail = ProductGenericView.as_view({'get': 'retrieve'})