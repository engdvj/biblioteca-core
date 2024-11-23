from django.shortcuts import render
from rest_framework.authtoken.models import Token

def dashboard(request):
    auth_token = request.COOKIES.get('auth_token')
    user_name = "Usuário"  # Valor padrão caso o token não seja válido
    if auth_token:
        try:
            token = Token.objects.get(key=auth_token)
            user_name = token.user.username  # Obtém o nome do usuário a partir do token
        except Token.DoesNotExist:
            pass

    return render(request, 'dashboard.html', {'user_name': user_name})
