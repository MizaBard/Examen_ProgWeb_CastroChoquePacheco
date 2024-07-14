from rest_framework import viewsets
from .models import Producto
from .serializer import ProductoSerializer



# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


# @api_view(['POST'])
# def crear_producto(request):
#     if request.method == 'POST':
#         serializer = ProductoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)