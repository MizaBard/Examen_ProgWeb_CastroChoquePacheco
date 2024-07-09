from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, info, portafolio, patreon, referencia, agregar_producto, listar_producto, modificar_producto, eliminar_producto, registro

urlpatterns = [
    path('', index, name="index"),
    path('info/', info, name="info"),
    path('portafolio/', portafolio, name="portafolio"),
    path('patreon/', patreon, name="patreon"),
    path('referencia/', referencia, name="referencia"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro")
]