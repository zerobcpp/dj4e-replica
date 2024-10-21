from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

import braintree
# Create your views here.

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='7f3bywsjqkbtpmg8',
    public_key='cx2s9cjkz97chwzz',
    private_key='262cacb7eed1415b4116499f2bc537b5'
  )
)


def validate_user(id, token):
  user_model = get_user_model()
  
  try:
    user = user_model.objects.get(pk=id)
    if user.session_token == token:
        return True
    return False
  except user_model.DoesNotExist:
    return JsonResponse("Not Valid User", safe=False)



@method_decorator(csrf_exempt, name='dispatch')
class Token(View):
  def get(self, id, token):
    if not validate_user(id, token):
        return JsonResponse("error", safe=False)
    return JsonResponse({'client_token': gateway.client_token.generate(), 'success':True})
  
  
@method_decorator(csrf_exempt, name='dispatch')
class Payment(View):
  def get(self): 
    pass
  def post(self, request, id, token):
    if not validate_user(id, token):
        return JsonResponse("error", safe=False)
    client_nonce = request.POST['payment_method_nonce']
    client_amount = request.POST['amount']
    
    result = gateway.transaction.sale({
        'amount': client_amount,
        'paymennt_method_nonce': client_nonce,
        'options':{
            "submit_for_settlement" : True,
        }
    })
    
    if result.is_success:
        return JsonResponse({'success':result.is_success, 
                            'transaction': {
                                'id': result.transaction.id,
                                'amount': result.transaction.amount,}
                            })
    
    return JsonResponse({'error': 'transaction error'})
  
  

  
  
    
  