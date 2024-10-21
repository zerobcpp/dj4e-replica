from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.OrderViewSet)

urlpatterns = [
    path('add/<int:id>/<str:token>/', views.OrderView.as_view(), name='addOrder'),
    path('', include(router.urls)),
]


