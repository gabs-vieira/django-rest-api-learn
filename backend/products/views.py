from django.shortcuts import get_object_or_404
from rest_framework import  authentication ,generics, mixins, permissions

from .models import Product
from .serializers import ProductSerializer
   
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404

"""
Lista de todos os APIViews e suas funções
CreateAPIView - POST serve para criar um novo objeto
ListAPIView - GET serve para listar todos os objetos
RetrieveAPIView - GET serve para pegar um objeto específico
DestroyAPIView - DELETE serve para deletar um objeto específico
UpdateAPIView - PUT serve para atualizar um objeto específico
RetrieveUpdateAPIView - GET e PUT serve para pegar e atualizar um objeto específico
RetrieveDestroyAPIView - GET e DELETE serve para pegar e deletar um objeto específico
RetrieveUpdateDestroyAPIView - GET, PUT e DELETE serve para pegar, atualizar e deletar um objeto específico
etc...
"""


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    #perform_create serve para fazer validações antes de salvar o objeto
    def perform_create(self, serializer):
        title = serializer.validate_data.get('title')
        content = serializer.validate_data.get('content') or None

        if content is None:
            content = title
        serializer.save()

product_list_create_view = ProductListCreateAPIView.as_view()



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() #Get the  query
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()



class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all() #Get the  query
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instante = serializer.save()


        if not instante.content:
            instante.content = instante.title
            instante.save()
            ##

product_update_view = ProductUpdateAPIView.as_view()




class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all() #Get the  query
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destoy(self, instance):
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()




class ProductMixinView(
        mixins.ListModelMixin, 
        generics.GenericAPIView,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        mixins.RetrieveModelMixin
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'# pk --> Primary Key pra que serve: 


    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs) # list --> Método do mixin que lista todos os objetos
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # create --> Método do mixin que cria um novo objeto
    
product_mixin_view = ProductMixinView.as_view()





@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None ,*args, **kwargs):

    # request = é o objeto que contém todas as informações da requisição
    # args = é uma lista de argumentos
    # kwargs = é um dicionário de argumentos

    method = request.method

    if method == "GET":

        # Get a product
        if pk is not None:

            # Primeiro método
            # Get a specific product
            # queryset = Product.objects.get(pk=pk)

            # if queryset:
            #     raise Http404("Product does not exist")
            # data = ProductSerializer(queryset).data


            # Segundo método
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data  # many=False --> Para serializar um único objeto
            return Response(data)
        
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data # many=True --> Para serializar uma lista de objetos o serializer serve para converter o objeto em um formato que pode ser convertido em JSON
        return Response(data)
        
    if method == "POST":
        # Create a new product
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True): # raize_exception --> Validator de required fields

            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None

            if content is None:
                content = title
            serializer.save(content=content)

            return Response(serializer.data)
        return Response( {"invalid": "not good data"}, status=400 )

