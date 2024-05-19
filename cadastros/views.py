from django.shortcuts import render
from django.views.generic import TemplateView


class CadProdView(TemplateView):
    template_name = "cadastros/cadproduto.html"
    
class CadClienteView(TemplateView):
    template_name = "cadastros/cadcliente.html"

