from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import CS

class CsList(ListView):
    
    model = CS
    template_name = 'rba/cs_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cs'] =  [(s.title ) for s in CS.objects.all()]
        return context

class CSDetailView(DetailView):

    model = CS
    template_name = 'rba/cs_detail.html'
    slug_field = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context

class baseDetailView(DetailView):

    model = CS
    template_name = 'base.html'
    slug_field = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cs'] =  [(s.title ) for s in CS.objects.all()]
        return context