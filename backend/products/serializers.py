from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # def create(self, validated_data):
    #     return super().create(validated_data) 
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

# get_ + nome do campo + _display é um padrão para criar um campo que exibe o valor de um campo de escolha
    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk }, request=request ) #reverse --> retorna a URL de uma view

    def get_my_discount(self, obj):
        try:

            if not hasattr(obj, 'id'):
                return None
            if not isinstance(obj, Product):
                return None
            return obj.get_discount()
        except:
            return None