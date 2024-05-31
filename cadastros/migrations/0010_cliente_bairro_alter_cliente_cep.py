# Generated by Django 4.2.13 on 2024-05-30 22:43

import cadastros.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_alter_cliente_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=9, validators=[cadastros.models.validate_cep], verbose_name='CEP:'),
        ),
    ]
