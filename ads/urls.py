from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    path('', views.adsListView.as_view(), name='all'),
    path('ads/<int:pk>', views.adsDetailView.as_view(), name='ads_detail'),
    path('ads/create', 
        views.adsCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_create'),
    path('ads/<int:pk>/update', 
        views.adsUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_update'),
    path('ads/<int:pk>/delete', 
        views.adsDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ads_delete'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
