from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name ='index'), #endereço, MinhaView.as_view(), nome da url 
]