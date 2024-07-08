from django.shortcuts import render
from .models import Producto, Usuario

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