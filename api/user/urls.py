from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='signin'),
    path('logout/<int:id>/', views.LogoutView.as_view(), name='signout'),
    path('', include(router.urls))
    
]
