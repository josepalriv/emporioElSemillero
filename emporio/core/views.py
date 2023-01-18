from django.shortcuts import render

# Create your views here.

def home(request):
    home_dict = {"insert_me": "Esto es la Página de Inicio"}
    return render(request, "core/home.html", context=home_dict)

def aboutUs(request):
    aboutUs_dict = {"insertame": "Aquí se describe el local, la dirección y redes sociales"}
    return render(request, "core/aboutus.html", context=aboutUs_dict)

def carrito(request):
    carrito_dict = {"insert_here": "Aquí va el detalle de compras y se formaliza el pago"}
    return render(request, "core/carrito.html", context=carrito_dict)