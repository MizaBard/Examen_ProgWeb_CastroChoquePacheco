from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return str(self.id)+" "+str(self.nombre)

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    contraseña = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.PositiveIntegerField(default=0)

    def __str__(self):
        return  str(self.rut)+" " +str(self.nombre)