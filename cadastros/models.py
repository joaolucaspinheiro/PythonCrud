from django.db import models

class Produto(models.Model):
    id_produto = models.BigAutoField(primary_key=True)
    nome_produto = models.CharField("Nome do produto", max_length=255, blank=False, unique=True)
    quantidade_produto = models.IntegerField("Quantidade do produto", blank=False)
    precocompra_produto = models.DecimalField("Preço de compra do produto", decimal_places=2, max_digits=6)
    precovenda_produto = models.DecimalField("Preço de venda do produto", decimal_places=2, max_digits=6)
    
    def __str__(self):
        return "{} ({})".format(self.nome_produto, self.quantidade_produto)
    
class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key =True)
    nome_cliente = models.CharField("Nome do cliente", max_length=255)
    email_cliente = models.EmailField("Email do cliente", max_length=254)
    cpf = models.CharField("CPF", max_length=11)
    telefone_cliente = models.CharField("Telefone do cliente", max_length=255)
    rua_endereco = models.CharField(max_length=50)
    numero_endereco = models.IntegerField()
    cidade_endereco = models.CharField(max_length=255)
    estado_edereco = models.CharField(max_length=255)
    data_nasc = models.DateField()
    
    def _str__(self):
        return "{} ({})".format(self.id, self.nome_cliente)
    
    
    
    
    