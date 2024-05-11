from django.urls import path
from .views import IndexView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name ='index'), #endereço, MinhaView.as_view(), nome da url 
    path('sobre/', SobreView.as_view(), name ='sobre'), 
    ]