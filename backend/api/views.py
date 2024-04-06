from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST' ])
def api_home(request, *args, **kwars):
    """
    DRF API VIEW
    """
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): # raize_exception --> Validator de required fields
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response( {"invalid": "not good data"}, status=400 )

# @api_view(["GET"])
# def api_home(request, *args, **kwars):
#     """
#     DRF API VIEW
#     """
#     instance = Product.objects.all().order_by("?").first()
#     data = {}

#     if instance:
#         # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
#         data = ProductSerializer(instance).data
#         return Response(data)
    










    """
        data = dict(data)
        json_data_str = json.dumps(data)
        return HttpResponse(json_data_str, headers={"content-type": "application/json"})
        model instance (model_data)
        turn a python dict
        return JSON to my client
    """