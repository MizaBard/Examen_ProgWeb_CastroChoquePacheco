from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Usuario
from .forms import ProductoForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def info(request):
    return render(request, 'web/infoChan.html')

def portafolio(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'web/portfolio.html', data)

def patreon(request):
    return render(request, 'web/patreon.html')

def registro(request):
    if request.method != "POST":
        usuario=Usuario.objects.all()
        context={ 'usuario' : usuario }
        return render(request, 'web/registro.html') 
    else: 
        rut = request.POST.get("rut")
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        contraseña = request.POST.get("contraseña")
        telefono = request.POST.get("telefono")

        usuario = Usuario.objects.create(rut=rut, nombre=nombre, email=email, contraseña=contraseña, telefono=telefono)
        usuario.save()
        return render(request, 'web/registro.html', {'success': True})  
    
def referencia(request):
    return render(request, 'web/BrutalismoAPI.html')

def login(request):
    return render (request, 'registration/login.html')

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

def listar_producto(request):

    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }

    return render(request, 'web/producto/listar.html', data)

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

def eliminar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_producto")