from rest_framework import serializers
from .models import Product
from api.category.models import Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        image = serializers.ImageField(max_length=None, allow_empty_file=False, 
                                allow_null=True, required=False)
        model = Product
        #fields = ['name', 'description', 'category', 'updated_at']
        fields = ['id', 'name', 'image', 'price', 'stock' ,'category', 'updated_at']