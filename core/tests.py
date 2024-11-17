from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token  # Import correto
from core.models.colecao import Colecao
from django.urls import reverse
from rest_framework.authtoken.models import Token
import logging

# Testes para Colecao
class ColecaoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_criar_nova_colecao(self):
        data = {'nome': 'Nova Coleção', 'descricao': 'Descrição da nova coleção'}
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 1)
        self.assertEqual(Colecao.objects.last().colecionador, self.user)

    def test_permissao_editar_colecao(self):
        outra_colecao = Colecao.objects.create(
            nome='Coleção de Teste',
            descricao='Descrição',
            colecionador=self.user
        )
        data = {'nome': 'Coleção Editada'}
        response = self.client.put(f'/colecoes/{outra_colecao.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        outra_colecao.refresh_from_db()
        self.assertEqual(outra_colecao.nome, 'Coleção Editada')

    def test_usuarios_nao_autenticados_nao_podem_criar_colecao(self):
        self.client.logout()
        data = {'nome': 'Coleção Sem Autenticação', 'descricao': 'Descrição'}
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_listagem_colecoes_para_usuario_autenticado(self):
        response = self.client.get('/colecoes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)

# Configuração do logger
logger = logging.getLogger(__name__)

# Testes para Login
class LoginTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Criação do usuário de teste
        self.user = User.objects.create_user(username='testuser', password='password')
        # Gera e salva o token
        self.token = Token.objects.create(user=self.user)

    def test_login_success(self):
        # Dados de login corretos
        data = {'username': 'testuser', 'password': 'password'}
        response = self.client.post(reverse('login'), data)  # Usando reverse para a URL
        
        # Logs para depuração
        print(f"Status Code: {response.status_code}")
        print(f"Response Data: {response.data}")
        print(f"Username: {self.user.username}")
        print(f"Password (hashed): {self.user.password}")
        
        # Verifica se a resposta é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se o token está presente na resposta
        self.assertIn('token', response.data)

    def test_login_failure(self):
        # Dados de login incorretos
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(reverse('login'), data)
        # Verifica se a resposta é 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)