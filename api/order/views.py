from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializers
from .models import Order
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.


def validate_user(id, token):
    user_model = get_user_model()
    user = get_object_or_404(user_model, pk=id)
    if token != user.session_token:
        return JsonResponse("error", safe=False)
    return user
    
@method_decorator(csrf_exempt, name='dispatch')
class OrderView(View):
    
    def get(self, id, token):
        return JsonResponse("Wrong method", safe=False)
    
    def post(self,request, id, token):
        user = validate_user(id, token)
        t_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']
        
        order = Order(user=user, product_name=products, 
                      total_amount=amount, transaction_id = t_id)
        order.save()
        return JsonResponse({"Status":"Success", "Message":"Order placed"})
        
        
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializers 