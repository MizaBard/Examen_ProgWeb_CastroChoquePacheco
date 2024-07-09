from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

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


# def registro(request):
#     if request.method != "POST":
#         usuario=Usuario.objects.all()
#         context={ 'usuario' : usuario }
#         return render(request, 'web/registro.html') 
#     else: 
#         rut = request.POST.get("rut")
#         nombre = request.POST.get("nombre")
#         email = request.POST.get("email")
#         contraseña = request.POST.get("contraseña")
#         telefono = request.POST.get("telefono")

#         usuario = Usuario.objects.create(rut=rut, nombre=nombre, email=email, contraseña=contraseña, telefono=telefono)
#         usuario.save()
#         return render(request, 'web/registro.html', {'success': True})  