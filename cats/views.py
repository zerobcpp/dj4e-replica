from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from cats.models import Cats, Breed
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def Home(response):
    return HttpResponse('Cats Page')

class CatList(LoginRequiredMixin, View):
    def get(self, request):
        breed = Breed.objects.all().count()
        cats = Cats.objects.all()
        print(cats)
        ctx = {'breed': breed, 'cat_list': cats}
        return render(request, 'cats/cats_list.html', ctx)
    
    def post(self, request):
        pass

class CatsListView(LoginRequiredMixin, generic.ListView):
    model = Cats
    
class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        breed = Breed.objects.all()
        content = {'breed': breed}
        return render(request, 'cats/breed_list.html', content)
    
class BreedAutoCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedAutoDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy('cats:all')

class BreedAutoUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
    
class CatsAutoCreate(LoginRequiredMixin, CreateView):
    model = Cats
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatsAutoDelete(LoginRequiredMixin, DeleteView):
    model = Cats
    fields = "__all__"
    success_url = reverse_lazy('cats:all')

class CatsAutoUpdate(LoginRequiredMixin, UpdateView):
    model = Cats
    fields = '__all__'
    success_url = reverse_lazy('cats:all')