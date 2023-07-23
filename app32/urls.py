from django.http import HttpResponse
from django.urls import re_path 
from app32 import views
app_name = 'app32'

urlpatterns = [
    re_path('', views.HomeView.as_view() ,name = 'home_page')
]
