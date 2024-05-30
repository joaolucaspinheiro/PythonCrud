from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Produto, Cliente
from django.urls import reverse_lazy
from django.contrib import messages

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome_produto','quantidade_produto', 'precocompra_produto', 'precovenda_produto',]
    template_name = "cadastros/cadproduto.html"
    success_url = reverse_lazy('listar-produto')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Produto cadastrado com sucesso!")
        return response
   
    
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
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Produto atualizado com sucesso!")
        return response
   
  
    
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome_cliente','data_nasc', 'cpf', 'email_cliente',
              'telefone','cep', 'estado', 'cidade', 'rua', 'numero']
    template_name = "cadastros/cadcliente.html"
    success_url = reverse_lazy('listar-cliente')
    
################## DELETE VIEW #################
    
class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "cadastros/form-excluirProduto.html"
    success_url = reverse_lazy('listar-produto')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Produto deletado com sucesso!")
        return response


    
class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cadastros/form-excluirCliente.html"
    success_url = reverse_lazy('listar-cliente')
    
    ################## LIST VIEW #################
    
class ProdutoList(ListView):
    model = Produto
    template_name = "cadastros/listas/produto.html"

    
class ClienteList(ListView):
    model = Cliente
    template_name = "cadastros/listas/cliente.html"


    