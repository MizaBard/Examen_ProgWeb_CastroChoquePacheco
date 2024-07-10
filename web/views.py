from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Boleta, detalle_boleta
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from web.carrito import Carrito

# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def info(request):
    return render(request, 'web/infoChan.html')


@login_required
def portafolio(request):
    
    busqueda = request.POST.get("buscar")
    productos = Producto.objects.all()

    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda) |
            Q(precio__icontains = busqueda)
        ).distinct()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 10)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity' : productos,
        'paginator' : paginator
    }

    return render(request, 'web/portfolio.html', data)


@login_required
def patreon(request):
    return render(request, 'web/patreon.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            login(request, user)

            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)
    
def referencia(request):
    return render(request, 'web/BrutalismoAPI.html')

def inicio(request, user):
    return render (request, 'registration/login.html')


@permission_required('web.add_producto')
def agregar_producto(request):

    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
        else:
            data["form"] = formulario

    return render(request, 'web/producto/agregar.html', data)


@permission_required('web.view_producto')
def listar_producto(request):

    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity' : productos,
        'paginator' : paginator
    }

    return render(request, 'web/producto/listar.html', data)


@permission_required('web.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_producto")
        data["form"] = formulario

    return render(request, 'web/producto/modificar.html', data)


@permission_required('web.delete_producto')
def eliminar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_producto")

def añadir_carrito(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito_compra.añadir(producto=producto)
    return redirect('portafolio')

def eliminar_carrito(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito_compra.eliminar_carrito(producto=producto)
    return redirect('portafolio')

def quitar_carrito(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito_compra.quitar(producto=producto)
    return redirect('portafolio')

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('portafolio')

def generarBoleta(request):
    precio_total = 0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
        producto = Producto.objects.get(id = value['id'])
        cant = value['cantidad']
        subtotal = cant * int(value['precio'])
        detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
        detalle.save()
        productos.append(detalle)
    datos= {
        'productos' : productos,
        'fecha' : boleta.fechaCompra,
        'total' : boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'web/detalleCarrito.html', datos)