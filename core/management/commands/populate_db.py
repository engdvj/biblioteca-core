from django.core.management.base import BaseCommand
from core.models import Category, Author, Book


class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        categoria_misterio = Category.objects.create(name="Mistério")
        categoria_ficcao = Category.objects.create(name="Ficção")
        categoria_fantasia = Category.objects.create(name="Fantasia")
        categoria_romance = Category.objects.create(name="Romance")

        autor_agatha_christie = Author.objects.create(name="Agatha Christie")
        autor_arthur_c_clarke = Author.objects.create(name="Arthur C. Clarke")
        autor_arthur_conan_doyle = Author.objects.create(name="Arthur Conan Doyle")
        autor_cs_lewis = Author.objects.create(name="C.S. Lewis")
        autor_emily_bronte = Author.objects.create(name="Emily Brontë")
        autor_george_rr_martin = Author.objects.create(name="George R.R. Martin")
        autor_isaac_asimov = Author.objects.create(name="Isaac Asimov")
        autor_jrr_tolkien = Author.objects.create(name="J.R.R. Tolkien")

        Book.objects.create(
            name="Assassinato no Expresso do Oriente",
            author=autor_agatha_christie,
            category=categoria_misterio,
            publication_date="1934-01-01",
        )
        Book.objects.create(
            name="Morte no Nilo",
            author=autor_agatha_christie,
            category=categoria_misterio,
            publication_date="1937-11-01",
        )
        Book.objects.create(
            name="2001: Uma Odisseia no Espaço",
            author=autor_arthur_c_clarke,
            category=categoria_ficcao,
            publication_date="1968-06-16",
        )
        Book.objects.create(
            name="Encontro com Rama",
            author=autor_arthur_c_clarke,
            category=categoria_ficcao,
            publication_date="1973-06-01",
        )
        Book.objects.create(
            name="O Cão dos Baskervilles",
            author=autor_arthur_conan_doyle,
            category=categoria_misterio,
            publication_date="1902-04-01",
        )
        Book.objects.create(
            name="Um Estudo em Vermelho",
            author=autor_arthur_conan_doyle,
            category=categoria_misterio,
            publication_date="1887-11-01",
        )
        Book.objects.create(
            name="As Crônicas de Nárnia",
            author=autor_cs_lewis,
            category=categoria_fantasia,
            publication_date="1950-10-16",
        )
        Book.objects.create(
            name="O Leão, a Feiticeira e o Guarda-Roupa",
            author=autor_cs_lewis,
            category=categoria_fantasia,
            publication_date="1950-10-16",
        )
        Book.objects.create(
            name="O Morro dos Ventos Uivantes",
            author=autor_emily_bronte,
            category=categoria_romance,
            publication_date="1847-12-01",
        )
        Book.objects.create(
            name="A Guerra dos Tronos",
            author=autor_george_rr_martin,
            category=categoria_fantasia,
            publication_date="1996-08-06",
        )
        Book.objects.create(
            name="A Fúria dos Reis",
            author=autor_george_rr_martin,
            category=categoria_fantasia,
            publication_date="1998-11-16",
        )
        Book.objects.create(
            name="Fundação",
            author=autor_isaac_asimov,
            category=categoria_ficcao,
            publication_date="1951-06-01",
        )
        Book.objects.create(
            name="Eu, Robô",
            author=autor_isaac_asimov,
            category=categoria_ficcao,
            publication_date="1950-12-02",
        )
        Book.objects.create(
            name="O Senhor dos Anéis",
            author=autor_jrr_tolkien,
            category=categoria_fantasia,
            publication_date="1954-07-29",
        )
        Book.objects.create(
            name="O Hobbit",
            author=autor_jrr_tolkien,
            category=categoria_fantasia,
            publication_date="1937-09-21",
        )
