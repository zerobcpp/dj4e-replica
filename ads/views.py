from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class adsListView(OwnerListView):
    model = Ad
    context_object_name = 'ads_list'
    # By convention:
    # template_name = "myarts/ads_list.html"


class adsDetailView(OwnerDetailView):
    model = Ad
    fields = ['title', 'text', 'price']


class adsCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price']


class adsUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']


class adsDeleteView(OwnerDeleteView):
    model = Ad
