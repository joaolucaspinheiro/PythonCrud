# Generated by Django 4.2.13 on 2024-05-26 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_alter_produto_precocompra_produto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=9, verbose_name='CEP:'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(blank=True, help_text='Informe apenas números', max_length=14, unique=True, verbose_name='CPF'),
        ),
    ]
