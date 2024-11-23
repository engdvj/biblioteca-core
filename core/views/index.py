from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token  # Importação necessária

def index(request):
    auth_token = request.COOKIES.get('auth_token')
    if auth_token:
        try:
            # Verifica se o token é válido
            Token.objects.get(key=auth_token)
            return redirect('/dashboard/')  # Redireciona para o dashboard
        except Token.DoesNotExist:
            pass  # Caso o token não exista, continua para o index.html
    return render(request, 'index.html')  # Renderiza a tela de login
