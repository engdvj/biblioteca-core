from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate

class Login(APIView):
    permission_classes = []  # Permite requisições sem autenticação

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Username e password são obrigatórios'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Autentica o usuário com as credenciais fornecidas
        user = authenticate(username=username, password=password)
        if user is not None:
            # Obtém o token existente ou cria um novo, se necessário
            token, created = Token.objects.get_or_create(user=user)
            # Aqui você pode executar o script ou lógica que precisa do token
            print(f"Token: {token.key}")  # Exemplo de uso do token

            # Retorna o token como resposta
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Credenciais inválidas'},
                status=status.HTTP_401_UNAUTHORIZED
            )
