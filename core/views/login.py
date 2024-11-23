from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate

class Login(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        auth_token = request.COOKIES.get('auth_token')
        if auth_token:
            try:
                Token.objects.get(key=auth_token)
                return redirect('/dashboard/')  # Redireciona para o dashboard
            except Token.DoesNotExist:
                pass
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username e password são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            response = Response({'redirect': '/dashboard/'}, status=status.HTTP_200_OK)  # Adiciona redirecionamento
            response.set_cookie(
                'auth_token', token.key, httponly=True, secure=False, samesite='Lax'
            )
            return response
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
