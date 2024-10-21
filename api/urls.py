from django.urls import path, include
from rest_framework.authtoken import views
from .views import HomePage
urlpatterns = [
     path('', HomePage.as_view(), name='api.home'),
     path('category/', include('api.category.urls')),
     path('product/', include('api.product.urls')),
     path('user/', include('api.user.urls')),
     path('order/', include('api.order.urls')), 
     path('paymennts/', include('api.payment.urls')),
     path('api-token-auth', views.obtain_auth_token, name='api-token-auth')
     
]
