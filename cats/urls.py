from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'cats'
urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('main/create/', views.CatsAutoCreate.as_view(), name='cats_create'),
    path('main/update/<int:pk>/', views.CatsAutoUpdate.as_view(), name='cats_update'),
    path('main/delete/<int:pk>', views.CatsAutoDelete.as_view(), name='cats_delete'),
    path('breed/', views.BreedList.as_view(), name='breed_list'),
    path('breed/create', views.BreedAutoCreate.as_view(), name='breed_create'),
    path('breed/update/<int:pk>', views.BreedAutoUpdate.as_view(), name='breed_update'),
    path('breed/delete/<int:pk>' , views.BreedAutoDelete.as_view(), name='breed_delete'),
]