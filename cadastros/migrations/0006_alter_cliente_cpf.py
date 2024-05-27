# Generated by Django 4.2.13 on 2024-05-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_alter_cliente_cep_alter_cliente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.IntegerField(blank=True, help_text='Informe apenas números', max_length=14, unique=True, verbose_name='CPF'),
        ),
    ]