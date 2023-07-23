from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse 
# Create your views here.


class HomeView(LoginRequiredMixin, View):
    template = 'home.html'
    def get(self, request):
        return render(request, self.template)
    
    def post(self, request):
        x = request.POST.get('field1').strip()
        y = request.POST.get('field2').strip()
        ctx = {'x': x[::-1], 'y': y[::-1]}
        return render(request, self.template, ctx)