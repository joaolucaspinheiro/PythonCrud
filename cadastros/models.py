from django.db import models
from django import forms
from django.core.exceptions import ValidationError
            
class Produto(models.Model):
    nome_produto = models.CharField("Nome:", max_length=255, blank=False, unique=True) 
    quantidade_produto = models.IntegerField("Quantidade:", blank=False)
    precocompra_produto = models.DecimalField("Preço de compra:", max_digits=6, decimal_places=2)
    precovenda_produto = models.DecimalField("Preço de venda:",max_digits=6, decimal_places=2)
    tipo = models.CharField(max_length=50, default="produto")
    
    
    def __str__(self):
        return "{} ({})UN".format(self.nome_produto, self.quantidade_produto)
    
def validate_cep(cep):
    cep = cep.replace('-','')
    if not cep.isdigit() or len(cep) != 8:
        raise ValidationError("O CEP está incompleto! ")
 
def validate_cpf(value):
        # Remove caracteres não numéricos
        cpf = value.replace('.', '').replace('-', '')
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValidationError('CPF deve conter 11 dígitos numéricos.')
        if len(set(cpf)) == 1:
            raise ValidationError('CPF inválido')
        soma = 0
        peso = 10
        for i in range(9):
            soma += int(cpf[i]) * peso
            peso -= 1
        resto = soma % 11
        if resto < 2:
            digito_verif1 = 0
        else:
            digito_verif1 = 11 - resto
    
        soma = 0
        peso = 11
        for i in range(10):
            soma += int(cpf[i]) * peso
            peso -= 1
        resto = soma % 11
        if resto < 2:
            digito_verif2 = 0
        else:
            digito_verif2 = 11 - resto
    
        if int(cpf[-2]) != digito_verif1 or int(cpf[-1]) != digito_verif2:
            raise ValidationError('CPF inválido')
        
class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key =True)
    nome_cliente = models.CharField("Nome:", max_length=255)
    email_cliente = models.EmailField("Email:", max_length=254)
    cpf = models.CharField("CPF", max_length=14, unique= True, help_text="Informe apenas números", validators=[validate_cpf])
    telefone = models.CharField("Telefone:", max_length=255, blank= True, unique= True)
    cep = models.CharField("CEP:", max_length=9, validators=[validate_cep]) 
    rua= models.CharField(max_length=50)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    bairro = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, default="cliente")
    
    def __str__(self):
        return "({}): {}".format(self.id_cliente, self.nome_cliente)
    
    def save(self, *args, **kwargs):
        # Remova a máscara do CPF antes de salvar
        self.cpf = self.cpf.replace('.', '').replace('-', '')
        super().save(*args, **kwargs)
        
        
    def format_cpf(self):
        # Formata o CPF para exibição
        if not self.cpf: 
            return''
        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'
    

    
    