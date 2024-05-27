from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Produto, Cliente
from django.urls import reverse_lazy

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome_produto','quantidade_produto', 'precocompra_produto', 'precovenda_produto',]
    template_name = "cadastros/cadproduto.html"
    success_url = reverse_lazy('listar-produto')
    
    
   
    
class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome_cliente','data_nasc', 'cpf', 'email_cliente',
              'telefone','cep', 'estado', 'cidade', 'rua', 'numero']
    template_name = "cadastros/cadcliente.html"
    success_url = reverse_lazy('listar-cliente')


################## UPDATE VIEW #################

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome_produto','quantidade_produto', 'precocompra_produto', 'precovenda_produto',]
    template_name = "cadastros/cadproduto.html"
    success_url = reverse_lazy('listar-produto')
    
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome_cliente','data_nasc', 'cpf', 'email_cliente',
              'telefone','cep', 'estado', 'cidade', 'rua', 'numero']
    template_name = "cadastros/cadcliente.html"
    success_url = reverse_lazy('listar-cliente')
    
################## DELETE VIEW #################
    
class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy('listar-produto')
    
class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy('listar-cliente')
    
    ################## LIST VIEW #################
    
class ProdutoList(ListView):
    model = Produto
    template_name = "cadastros/listas/produto.html"

    
class ClienteList(ListView):
    model = Cliente
    template_name = "cadastros/listas/cliente.html"


    