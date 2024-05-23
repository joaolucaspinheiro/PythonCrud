from django.db import models
from django.core.exceptions import ValidationError

            
class Produto(models.Model):
    nome_produto = models.CharField("Nome:", max_length=255, blank=False, unique=True) 
    quantidade_produto = models.IntegerField("Quantidade:", blank=False)
    precocompra_produto = models.DecimalField("Preço de compra:", decimal_places=2, max_digits=6)
    precovenda_produto = models.DecimalField("Preço de venda:", decimal_places=2, max_digits=6)
    
    
    def __str__(self):
        return "{} ({})".format(self.nome_produto, self.quantidade_produto)
    
class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key =True)
    nome_cliente = models.CharField("Nome:", max_length=255)
    email_cliente = models.EmailField("Email:", max_length=254)
    cpf = models.CharField("CPF", max_length=11, blank= True, unique= True, help_text="Informe apenas números")
    telefone = models.CharField("Telefone:", max_length=255, blank= True, unique= True)
    cep = models.CharField("CEP:", max_length=8) 
    rua= models.CharField(max_length=50)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    
   
        
    
    def _str__(self):
        return "{} ({})".format(self.id, self.nome_cliente)

    
    
    
    