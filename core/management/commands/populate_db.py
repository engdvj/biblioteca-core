from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro


class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        categoria_misterio = Categoria.objects.create(nome="Mistério")
        categoria_ficcao = Categoria.objects.create(nome="Ficção")
        categoria_fantasia = Categoria.objects.create(nome="Fantasia")
        categoria_romance = Categoria.objects.create(nome="Romance")

        autor_agatha_christie = Autor.objects.create(nome="Agatha Christie")
        autor_arthur_c_clarke = Autor.objects.create(nome="Arthur C. Clarke")
        autor_arthur_conan_doyle = Autor.objects.create(nome="Arthur Conan Doyle")
        autor_cs_lewis = Autor.objects.create(nome="C.S. Lewis")
        autor_emily_bronte = Autor.objects.create(nome="Emily Brontë")
        autor_george_rr_martin = Autor.objects.create(nome="George R.R. Martin")
        autor_isaac_asimov = Autor.objects.create(nome="Isaac Asimov")
        autor_jrr_tolkien = Autor.objects.create(nome="J.R.R. Tolkien")

        Livro.objects.create(
            nome="Assassinato no Expresso do Oriente",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            data_publicacao="1934-01-01",
        )
        Livro.objects.create(
            nome="Morte no Nilo",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            data_publicacao="1937-11-01",
        )
        Livro.objects.create(
            nome="2001: Uma Odisseia no Espaço",
            autor=autor_arthur_c_clarke,
            categoria=categoria_ficcao,
            data_publicacao="1968-06-16",
        )
        Livro.objects.create(
            nome="Encontro com Rama",
            autor=autor_arthur_c_clarke,
            categoria=categoria_ficcao,
            data_publicacao="1973-06-01",
        )
        Livro.objects.create(
            nome="O Cão dos Baskervilles",
            autor=autor_arthur_conan_doyle,
            categoria=categoria_misterio,
            data_publicacao="1902-04-01",
        )
        Livro.objects.create(
            nome="Um Estudo em Vermelho",
            autor=autor_arthur_conan_doyle,
            categoria=categoria_misterio,
            data_publicacao="1887-11-01",
        )
        Livro.objects.create(
            nome="As Crônicas de Nárnia",
            autor=autor_cs_lewis,
            categoria=categoria_fantasia,
            data_publicacao="1950-10-16",
        )
        Livro.objects.create(
            nome="O Leão, a Feiticeira e o Guarda-Roupa",
            autor=autor_cs_lewis,
            categoria=categoria_fantasia,
            data_publicacao="1950-10-16",
        )
        Livro.objects.create(
            nome="O Morro dos Ventos Uivantes",
            autor=autor_emily_bronte,
            categoria=categoria_romance,
            data_publicacao="1847-12-01",
        )
        Livro.objects.create(
            nome="A Guerra dos Tronos",
            autor=autor_george_rr_martin,
            categoria=categoria_fantasia,
            data_publicacao="1996-08-06",
        )
        Livro.objects.create(
            nome="A Fúria dos Reis",
            autor=autor_george_rr_martin,
            categoria=categoria_fantasia,
            data_publicacao="1998-11-16",
        )
        Livro.objects.create(
            nome="Fundação",
            autor=autor_isaac_asimov,
            categoria=categoria_ficcao,
            data_publicacao="1951-06-01",
        )
        Livro.objects.create(
            nome="Eu, Robô",
            autor=autor_isaac_asimov,
            categoria=categoria_ficcao,
            data_publicacao="1950-12-02",
        )
        Livro.objects.create(
            nome="O Senhor dos Anéis",
            autor=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            data_publicacao="1954-07-29",
        )
        Livro.objects.create(
            nome="O Hobbit",
            autor=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            data_publicacao="1937-09-21",
        )
