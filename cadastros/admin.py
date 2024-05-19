from django.contrib import admin

#importando minhas classes
from .models import Cliente, Produto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Produto)