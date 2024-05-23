from django.views.generic import CreateView
from .models import Produto, Cliente
from django.urls import reverse_lazy

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome_produto',
              'quantidade_produto', 'precocompra_produto', 'precovenda_produto',]
    template_name = "cadastros/cadproduto.html"
    success_url = reverse_lazy('index')
   
    
class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome_cliente','data_nasc', 'cpf', 'email_cliente',
              'telefone','cep', 'estado', 'cidade', 'rua', 'numero']
    template_name = "cadastros/cadcliente.html"

