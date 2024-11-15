from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Username e password são obrigatórios'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Log para verificar os dados recebidos
        logger.debug(f"Recebido username: {username}, password: {password}")

        # Autenticar o usuário
        user = authenticate(username=username, password=password)

        if user is not None:
            # Login do usuário
            login(request, user)

            # Gerar ou pegar o token do usuário
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Log para quando as credenciais forem inválidas
            logger.warning(f"Falha na autenticação para username: {username}")
            return Response(
                {'error': 'Credenciais inválidas'},
                status=status.HTTP_401_UNAUTHORIZED
            )
