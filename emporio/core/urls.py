from django.urls import path
from .views import home, aboutUs, carrito, formulario_ingresa_producto, login, base, registro_usuario

app_name = 'core'
urlpatterns = [
    path('', home, name="home"),
    path('nosotros/', aboutUs, name="Nuestra Tienda"),
    path('login/', login, name="Inicio de Sesion"),
    path('pago/', carrito, name="Carrito de Compras"),
    path('formulario/', formulario_ingresa_producto, name="Formulario de Productos"),
    path('base/', base, name="Base de Prueba"),
    path('registro/', registro_usuario, name="Registro de Usuario"),

]