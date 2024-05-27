from django.urls import path
from .views import ProdutoCreate, ClienteCreate
from .views import ProdutoUpdate, ClienteUpdate
from .views import ProdutoDelete, ClienteDelete
from .views import ProdutoList, ClienteList

urlpatterns = [
    #############URLS PARA CADASTRAR #############
    path('cadastrar-produto/', ProdutoCreate.as_view(), name ='cadastrar-produto'),
    path('cadastrar-cliente/', ClienteCreate.as_view(), name ='cadastrar-cliente'),
    
    #############URLS PARA EDITAR #############
    path('editar/produto/<int:pk>',ProdutoUpdate.as_view(), name ='editar-produto'),
    path('editar/cliente/<int:pk>', ClienteUpdate.as_view(), name ='editar-cliente'),
    
    #############URLS PARA EXCLUIR #############
    
    path('excluir/produto/<int:pk>',ProdutoDelete.as_view(), name ='excluir-produto'),
    path('excluir/cliente/<int:pk>', ClienteDelete.as_view(), name ='excluir-cliente'),
    
    #############URLS PARA LISTAR #############
    
    path('listar/produto/', ProdutoList.as_view(), name ='listar-produto'),
    path('listar/cliente/', ClienteList.as_view(), name ='listar-cliente'),
    ]