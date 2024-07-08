from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, info, portafolio, patreon, registro, referencia, login

urlpatterns = [
    path('', index, name="index"),
    path('info/', info, name="info"),
    path('portafolio/', portafolio, name="portafolio"),
    path('patreon/', patreon, name="patreon"),
    path('registro/', registro, name="registro"),
    path('referencia/', referencia, name="referencia"),
    path('registration/login', login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]