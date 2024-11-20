from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from core.models.colecao import Colecao
from django.urls import reverse
from core.models.autor import Autor
from core.models.categoria import Categoria
from core.models.livro import Livro
from core.serializers.autor import AutorSerializer
from core.serializers.categoria import CategoriaSerializer
from core.serializers.colecao import ColecaoSerializer
from core.serializers.livro import LivroSerializer
from django.test.client import RequestFactory
from rest_framework.permissions import BasePermission
from core.permisions.custom_permissions import IsColecionador
from django.core.management import execute_from_command_line
from django.test import RequestFactory



class ColecaoTests(TestCase):
    """
    Testes relacionados à funcionalidade de coleções.
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_criar_nova_colecao(self):
        """
        Testa se uma nova coleção é criada e associada ao usuário autenticado.
        """
        data = {'nome': 'Nova Coleção', 'descricao': 'Descrição da nova coleção'}
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 1)
        self.assertEqual(Colecao.objects.last().colecionador, self.user)

    def test_criar_colecao_sem_nome(self):
        """
        Testa se uma coleção sem nome não pode ser criada.
        """
        data = {'descricao': 'Descrição sem nome'}
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_permissao_editar_colecao(self):
        """
        Testa se o colecionador pode editar sua própria coleção.
        """
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
        """
        Testa se um usuário diferente não pode editar a coleção de outro usuário.
        """
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
        """
        Testa se usuários não autenticados não podem criar coleções.
        """
        self.client.logout()
        data = {'nome': 'Coleção Sem Autenticação', 'descricao': 'Descrição'}
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_usuarios_nao_autenticados_nao_podem_editar_colecao(self):
        """
        Testa se usuários não autenticados não podem editar coleções.
        """
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
        """
        Testa se as coleções estão visíveis para usuários autenticados.
        """
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

    def test_listagem_colecoes_para_usuario_nao_autenticado(self):
        """
        Testa se usuários não autenticados podem visualizar coleções públicas.
        """
        self.client.logout()
        response = self.client.get('/colecoes/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_deletar_colecao(self):
        """
        Testa se o colecionador pode deletar sua própria coleção.
        """
        colecao = Colecao.objects.create(
            nome='Coleção de Teste',
            descricao='Descrição',
            colecionador=self.user
        )
        response = self.client.delete(f'/colecoes/{colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Colecao.objects.count(), 0)

    def test_outro_usuario_nao_pode_deletar_colecao(self):
        """
        Testa se um usuário diferente não pode deletar a coleção de outro usuário.
        """
        outro_usuario = User.objects.create_user(username='outro', password='password')
        outra_colecao = Colecao.objects.create(
            nome='Coleção de Outro Usuário',
            descricao='Descrição',
            colecionador=outro_usuario
        )
        response = self.client.delete(f'/colecoes/{outra_colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class GeneralSerializerTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/')

        self.user = User.objects.create_user(username='testuser', password='password')
        self.autor = Autor.objects.create(nome="Agatha Christie")
        self.categoria = Categoria.objects.create(nome="Ficção")
        self.livro1 = Livro.objects.create(
            nome="Assassinato no Expresso do Oriente",
            autor=self.autor,
            categoria=self.categoria,
            data_publicacao="1934-01-01",
            publicado=True,
        )
        self.livro2 = Livro.objects.create(
            nome="Morte no Nilo",
            autor=self.autor,
            categoria=self.categoria,
            data_publicacao="1937-01-01",
            publicado=True,
        )
        self.colecao = Colecao.objects.create(
            nome="Coleção Clássica",
            descricao="Livros clássicos de mistério",
            colecionador=self.user,
        )
        self.colecao.livros.set([self.livro1, self.livro2])

    def test_autor_serializer(self):
        serializer = AutorSerializer(instance=self.autor, context={'request': self.request})
        data = serializer.data
        self.assertEqual(data['id'], self.autor.id)
        self.assertEqual(data['nome'], self.autor.nome)
        self.assertEqual(len(data['livros']), 2)

    def test_categoria_serializer(self):
        serializer = CategoriaSerializer(instance=self.categoria, context={'request': self.request})
        data = serializer.data
        self.assertEqual(data['id'], self.categoria.id)
        self.assertEqual(data['nome'], self.categoria.nome)
        self.assertEqual(len(data['livros']), 2)

    def test_colecao_serializer(self):
        serializer = ColecaoSerializer(instance=self.colecao, context={'request': self.request})
        data = serializer.data
        self.assertEqual(data['id'], self.colecao.id)
        self.assertEqual(data['nome'], self.colecao.nome)
        self.assertEqual(len(data['livros']), 2)

    def test_livro_serializer(self):
        serializer = LivroSerializer(instance=self.livro1, context={'request': self.request})
        data = serializer.data
        self.assertEqual(data['id'], self.livro1.id)
        self.assertEqual(data['nome'], self.livro1.nome)
        self.assertEqual(data['autor']['nome'], self.autor.nome)
        self.assertEqual(data['categoria']['nome'], self.categoria.nome)
        self.assertEqual(data['data_publicacao'], "1934-01-01")  # Formato correto da data
        self.assertTrue(data['publicado'])

    def test_colecao_create(self):
        data = {
            "nome": "Nova Coleção",
            "descricao": "Descrição",
            "livros_selecao": [self.livro1.id, self.livro2.id],
        }
        serializer = ColecaoSerializer(data=data, context={'request': self.request})
        self.assertTrue(serializer.is_valid())
        colecao = serializer.save(colecionador=self.user)
        self.assertEqual(colecao.nome, data['nome'])
        self.assertEqual(colecao.livros.count(), 2)

    def test_livro_create(self):
        data = {
            "nome": "Novo Livro",
            "autor_selecao": self.autor.id,
            "categoria_selecao": self.categoria.id,
            "data_publicacao": "2024-01-01T00:00:00",
            "publicado": False,
        }
        serializer = LivroSerializer(data=data, context={'request': self.request})
        self.assertTrue(serializer.is_valid())
        livro = serializer.save()
        self.assertEqual(livro.nome, data['nome'])
        self.assertEqual(livro.autor, self.autor)
        self.assertEqual(livro.categoria, self.categoria)
        
        
class CustomAuthenticationTests(TestCase):
    def test_has_permission(self):
        permission = IsColecionador()
        self.assertTrue(hasattr(permission, 'has_permission'))
        self.assertIsInstance(permission, BasePermission)
        
class CustomPermissionsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='colecionador', password='password')
        self.other_user = User.objects.create_user(username='outro_usuario', password='password')
        self.colecao = Colecao.objects.create(
            nome='Minha Coleção',
            descricao='Descrição da coleção',
            colecionador=self.user
        )

    def test_is_colecionador(self):
        permission = IsColecionador()

        # Caso 1: Leitura permitida para todos
        request = self.factory.get('/')
        request.user = self.other_user
        self.assertTrue(permission.has_object_permission(request, None, self.colecao))

        # Caso 2: Modificação permitida apenas para o colecionador
        request = self.factory.put('/')
        request.user = self.user
        self.assertTrue(permission.has_object_permission(request, None, self.colecao))

        # Caso 3: Modificação negada para outro usuário
        request.user = self.other_user
        self.assertFalse(permission.has_object_permission(request, None, self.colecao))

class ApiRaizTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_api_raiz(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('coleções', response.data)  # Atualizado para refletir a chave correta


        
class AutoresViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.autor = Autor.objects.create(nome="Autor Teste")

    def test_listar_autores(self):
        response = self.client.get('/autores/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_detalhes_autor(self):
        response = self.client.get(f'/autores/{self.autor.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['nome'], "Autor Teste")
        
        
class LivrosViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.autor = Autor.objects.create(nome="Autor Teste")
        self.categoria = Categoria.objects.create(nome="Categoria Teste")
        self.livro = Livro.objects.create(
            nome="Livro Teste",
            autor=self.autor,
            categoria=self.categoria,
            data_publicacao="2024-01-01",
            publicado=True
        )

    def test_listar_livros(self):
        response = self.client.get('/livros/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_detalhes_livro(self):
        response = self.client.get(f'/livros/{self.livro.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['nome'], "Livro Teste")
        
class IndexViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Login - Biblioteca API</title>', response.content)
        
class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.token, _ = Token.objects.get_or_create(user=self.user)

    def test_login_success(self):
        response = self.client.post('/api/login/', {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('auth_token', response.cookies)

    def test_login_failure(self):
        response = self.client.post('/api/login/', {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        
class ManagePyTests(TestCase):
    def test_manage_py_runs(self):
        # Testa se o comando "help" roda sem erros
        try:
            execute_from_command_line(['manage.py', 'help'])
        except SystemExit as e:
            self.assertEqual(e.code, 0)