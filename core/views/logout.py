from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

class Logout(APIView):
    permission_classes = []  # Remove autenticação para esta view

    def post(self, request, *args, **kwargs):
        response = Response({'message': 'Logout bem-sucedido'}, status=status.HTTP_200_OK)
        response.delete_cookie('auth_token')  # Remove o cookie de autenticação
        return response

    def get(self, request, *args, **kwargs):
        return redirect('/')
