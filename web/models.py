from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    contraseña = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.PositiveIntegerField(default=0)

    def __str__(self):
        return  str(self.rut)+" " +str(self.nombre)+ " "+ str(self.email)+" "+str(self.contraseña)+" "+ str(self.telefono)