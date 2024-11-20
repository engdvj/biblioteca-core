from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from core.models.colecao import Colecao
from django.urls import reverse


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
        colecao = Colecao.objects.create(
            nome='Coleção de Teste',
            descricao='Descrição',
            colecionador=self.user
        )
        data = {'nome': 'Coleção Editada'}
        response = self.client.put(f'/colecoes/{colecao.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        colecao.refresh_from_db()
        self.assertEqual(colecao.nome, 'Coleção Editada')

    def test_outro_usuario_nao_pode_editar_colecao(self):
        outro_usuario = User.objects.create_user(username='outro', password='password')
        outra_colecao = Colecao.objects.create(
            nome='Coleção de Outro Usuário',
            descricao='Descrição',
            colecionador=outro_usuario
        )
        data = {'nome': 'Tentativa de Edição'}
        response = self.client.put(f'/colecoes/{outra_colecao.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_usuarios_nao_autenticados_nao_podem_criar_colecao(self):
        self.client.logout()
        data = {'nome': 'Coleção Sem Autenticação', 'descricao': 'Descrição'}
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_usuarios_nao_autenticados_nao_podem_editar_colecao(self):
        colecao = Colecao.objects.create(
            nome='Coleção do Usuário',
            descricao='Descrição',
            colecionador=self.user
        )
        self.client.logout()
        data = {'nome': 'Tentativa de Edição'}
        response = self.client.put(f'/colecoes/{colecao.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_listagem_colecoes_para_usuario_autenticado(self):
        Colecao.objects.create(
            nome='Coleção do Usuário',
            descricao='Minha coleção',
            colecionador=self.user
        )
        outro_usuario = User.objects.create_user(username='outro', password='password')
        Colecao.objects.create(
            nome='Coleção de Outro Usuário',
            descricao='Outra coleção',
            colecionador=outro_usuario
        )
        response = self.client.get('/colecoes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_deletar_colecao(self):
        colecao = Colecao.objects.create(
            nome='Coleção de Teste',
            descricao='Descrição',
            colecionador=self.user
        )
        response = self.client.delete(f'/colecoes/{colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Colecao.objects.count(), 0)

    def test_outro_usuario_nao_pode_deletar_colecao(self):
        outro_usuario = User.objects.create_user(username='outro', password='password')
        outra_colecao = Colecao.objects.create(
            nome='Coleção de Outro Usuário',
            descricao='Descrição',
            colecionador=outro_usuario
        )
        response = self.client.delete(f'/colecoes/{outra_colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LoginTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.create_user(username='testuser', password='password')
        cls.token, _ = Token.objects.get_or_create(user=cls.user)

    def test_login_success(self):
        data = {'username': 'testuser', 'password': 'password'}
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_failure(self):
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
