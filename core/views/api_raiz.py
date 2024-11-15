from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ApiRaiz(APIView):
    authentication_classes = [TokenAuthentication]  # Autenticação baseada em token
    permission_classes = [IsAuthenticated]  # Exige que o usuário esteja autenticado

    def get(self, request, *args, **kwargs):
        return Response({"message": "Acesso permitido com autenticação"})
