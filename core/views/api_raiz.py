from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class ApiRaiz(APIView):
    name = "Biblioteca API - Endpoints Principais"

    def get(self, request, *args, **kwargs):
        context = {
            "Listas": [
                {
                    "nome": "Autores",
                    "endpoint": reverse('lista-autores', request=request),
                    "descrição": "Lista todos os autores."
                },
                {
                    "nome": "Livros",
                    "endpoint": reverse('lista-livros', request=request),
                    "descrição": "Lista todos os livros."
                },
                {
                    "nome": "Categorias",
                    "endpoint": reverse('lista-categorias', request=request),
                    "descrição": "Lista todas as categorias."
                }
            ],
            "Detalhes": [
                {
                    "nome": "Autor",
                    "endpoint": "/api/autores/{id}/",
                    "descrição": "Obtém, atualiza ou deleta um autor específico pelo ID."
                },
                {
                    "nome": "Livro",
                    "endpoint": "/api/livros/{id}/",
                    "descrição": "Obtém, atualiza ou deleta um livro específico pelo ID."
                },
                {
                    "nome": "Categoria",
                    "endpoint": "/api/categorias/{id}/",
                    "descrição": "Obtém, atualiza ou deleta uma categoria específica pelo ID."
                }
            ]
        }
        return Response(context)
