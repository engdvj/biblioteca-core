from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Rota para o painel de administração do Django
    path('admin/', admin.site.urls),

    # Inclui as URLs do aplicativo 'core'
    path('', include('core.urls')),

    # Endpoint para obtenção de token de autenticação
    path('token/', obtain_auth_token, name='obtain-token'),
]


