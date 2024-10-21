from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Order

class OrderSerializers(HyperlinkedModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'