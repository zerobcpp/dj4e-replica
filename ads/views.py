from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

from ads.forms import CreateForm
from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class adsListView(OwnerListView):
    model = Ad
    context_object_name = 'ads_list'
    # By convention:
    # template_name = "myarts/ads_list.html"


class adsDetailView(OwnerDetailView):
    model = Ad
    fields = ['title', 'text', 'price', 'picture']



class adsCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price', 'picture']
    success_url = reverse_lazy('pics:all')
    template_name = 'ads/Ad_form.html'
    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)


class adsUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price', 'picture']
    success_url = reverse_lazy('pics:all')
    template_name = 'ads/Ad_form.html'
    def get(self, request, pk):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)


class adsDeleteView(OwnerDeleteView):
    model = Ad

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    print(ad)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response

