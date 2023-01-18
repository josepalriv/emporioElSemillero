from django.urls import path
from .views import home, aboutUs, carrito

urlpatterns = [
    path('', home, name="home"),
    path('nosotros/', aboutUs, name="Nuestra Tienda"),
    path('pago', carrito, name="Carrito de Compras"),
]