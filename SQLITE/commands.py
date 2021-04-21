import click
from database import Database
from os import getenv  # Getenv pozwala nam przekazac zmienne z .env


@click.group()
def cli():
    pass


@click.command()
def setup():
    print('Tworze tabele w bazie danych')
    db = Database(getenv('DB_NAME'))  # Tworzymy obiekt Database, nazwe przekazujemy poprzez getenv
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')


@click.command()
@click.argument('category')
@click.argument('url')
def add(category: str, url: str):
    print('Dodaje nowy adres url')
    db = Database(getenv('DB_NAME'))
    db.insert('urls', None, category, url)  # wykonujemy polecenie


@click.command(name='categories')
def fetch_categories():  # Definiujemy funkcje printujaca nam liste kategorii w bazie
    print('Lista kategorii')
    db = Database(getenv('DB_NAME'))
    categories = db.fetch_distinct('urls', 'category')

    for name in categories:
        print(name)


@click.command()
@click.argument('category')
def index(category: str):
    db = Database(getenv('DB_NAME'))
    links = db.fetch_all('urls', category=category)

    for link in links:
        print(link[2])
