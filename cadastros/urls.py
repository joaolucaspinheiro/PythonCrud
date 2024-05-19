from django.urls import path
from .views import CadProdView, CadClienteView

urlpatterns = [
    path('produto/', CadProdView.as_view(), name ='produto'),
    path('cliente/', CadClienteView.as_view(), name ='cliente'),
    ]