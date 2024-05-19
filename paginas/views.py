from django.views.generic import TemplateView
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"



