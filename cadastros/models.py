from django.db import models
from django import forms
            
class Produto(models.Model):
    nome_produto = models.CharField("Nome:", max_length=255, blank=False, unique=True) 
    quantidade_produto = models.IntegerField("Quantidade:", blank=False)
    precocompra_produto = models.DecimalField("Preço de compra:", max_digits=6, decimal_places=2)
    precovenda_produto = models.DecimalField("Preço de venda:",max_digits=6, decimal_places=2)
    
    
    def __str__(self):
        return "{} ({})UN".format(self.nome_produto, self.quantidade_produto)
    
class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key =True)
    nome_cliente = models.CharField("Nome:", max_length=255)
    email_cliente = models.EmailField("Email:", max_length=254)
    cpf = models.CharField("CPF", max_length=14, blank= True, unique= True, help_text="Informe apenas números")
    telefone = models.CharField("Telefone:", max_length=255, blank= True, unique= True)
    cep = models.CharField("CEP:", max_length=9) 
    rua= models.CharField(max_length=50)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    
    def __str__(self):
        return "{} ({})".format(self.id_cliente, self.nome_cliente)

    
    
    
    