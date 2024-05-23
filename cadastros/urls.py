from django.urls import path
from .views import ProdutoCreate, ClienteCreate

urlpatterns = [
    path('produto/', ProdutoCreate.as_view(), name ='produto'),
    path('cliente/', ClienteCreate.as_view(), name ='cliente'),
    ]