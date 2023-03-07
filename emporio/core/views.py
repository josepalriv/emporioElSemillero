from django.shortcuts import render
from .models import Producto
from .forms import FormularioIngresoProducto, UserForm


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

            if 'foto' in request.FILES:
                formulario.foto = request.FILES['foto']
            formulario.save()
            return home(request)
        else:
            print('ERROR, FORMULARIO INVALIDO')

    return render(request, "core/formulario.html", {'formulario':formulario})

def registro_usuario(request):

    registrado = False

    if request.method == "POST":
        form_usuario = UserForm(data=request.POST)

        if form_usuario.is_valid():
            user = form_usuario.save()
            user.set_password(user.password)
            user.save()
            registrado = True
        else:
            print(form_usuario.errors)
    else:
        form_usuario = UserForm()

    return render(request, 'core/registro.html',{'formulario_usuario':form_usuario, 'registrado':registrado})
