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