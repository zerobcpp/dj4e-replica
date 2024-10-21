from django.urls import path, include
from .views import Token, Payment

urlpatterns = [
    path('gettokken/<int:id>/<str:token>/', Token.as_view(), name='get_token'),
    path('payment/<int:id>/<str:token>/', Payment.as_view(), name='process_payment'), 
]
