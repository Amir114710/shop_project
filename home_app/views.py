from django.shortcuts import render
from django.views.generic.base import TemplateView 



class HomeView(TemplateView):
    template_name = 'home_app/index.html'
