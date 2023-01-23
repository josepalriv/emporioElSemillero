from django.shortcuts import render
from .models import Producto, Categoria
from . import forms
from .forms import FormularioIngresoProducto


# Create your views here.
def base(request):
    aboutUs_dict = {"insertame": "Este es el template de la página web"}
    return render(request, "core/base.html", context=aboutUs_dict)

def home(request):
    lista_productos = Producto.objects.order_by('codigo')
    producto_dict = {"productos": lista_productos}
    return render(request, "core/home.html", context=producto_dict)

def aboutUs(request):
    aboutUs_dict = {"insertame": "Aquí se describe el local, la dirección y redes sociales"}
    return render(request, "core/aboutus.html", context=aboutUs_dict)

def login(request):
    login_dict = {"insertame": "Aquí inician sesión los trabajadores y clientes de la tienda"}
    return render(request, "core/login.html", context=login_dict)

def carrito(request):
    carrito_dict = {"insertame": "Aquí va el detalle de compras y se formaliza el pago"}
    return render(request, "core/carrito.html", context=carrito_dict)

def formulario_ingresa_producto(request):
    formulario = FormularioIngresoProducto()

    if request.method == "POST":
        formulario = FormularioIngresoProducto(request.POST)

        if formulario.is_valid():
            formulario.save(commit=True)
            return home(request)
        else:
            print('ERROR, FORMULARIO INVALIDO')

    return render(request, "core/formulario.html", {'formulario':formulario})
