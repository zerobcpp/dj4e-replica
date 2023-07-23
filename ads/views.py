from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.db.models import Q


from ads.forms import CreateForm, CommentForm
from ads.models import Ad, Comment, Fav
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView



class adsListView(OwnerListView):
    model = Ad
    template_name = 'ads/Ad_list.html'
    def get(self, request):
        s_tag = request.GET.get('search', None)
        if s_tag:
            query = Q(title__icontains=s_tag)
            query.add(Q(text__icontains=s_tag), Q.OR)
            query.add(Q(tags__name__in=[s_tag]), Q.OR)
            ads = Ad.objects.filter(query).select_related().distinct().order_by('-updated_at')[:10]
        else:
            ads = Ad.objects.all().order_by('-create_at')
        favorites = []
        if request.user.is_authenticated:
            #attr = request.user.__dir__()
            rows = request.user.Favorite_ads.values('id')
            for r in rows:
                favorites.append(r['id'])
            
        ctx = {'ads_list':ads, 'favorites':favorites}
        return render(request, self.template_name, ctx)
        
        

class adsDetailView(OwnerDetailView):
    template = 'ads/Ad_detail.html'
    def get(self, request, pk):
        obj = Ad.objects.get(id=pk)

        comments = Comment.objects.filter(ad=obj).order_by('-updated_at')
        comment_form = CommentForm()
        ctx = {'ad': obj, 'cform':comment_form, 'comments':comments}
        return render(request, self.template, ctx)
        


class adsCreateView(OwnerCreateView):
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
        form.save_m2m()
        return redirect(self.success_url)


class adsUpdateView(OwnerUpdateView):
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
        form.save_m2m()
        return redirect(self.success_url)


class adsDeleteView(OwnerDeleteView):
    model = Ad

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response


class CommentCreateView(OwnerCreateView):
    def post(self, request, pk):
            ad = get_object_or_404(Ad, id=pk)
            comment = Comment(text=request.POST['comment'], owner=request.user, ad=ad)
            comment.save()
            return redirect(reverse('ads:ads_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = 'comment\delete.html'
    
    def get_success_url(self) -> str:
        id = self.object.ad.id
        return reverse_lazy('ads:ads_detail', args=[id])

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        a = get_object_or_404(Ad, id=pk)
        fav = Fav(user=request.user, ad = a)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            print('Some key existed already')
            pass
        return JsonResponse({'favored': pk})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        ads = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, ad = ads).delete()
        except Fav.DoesNotExist as e:
            pass

        return JsonResponse({'unfavored': pk})

    
    