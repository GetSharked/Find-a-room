from database import Database
from sys import argv
from os import getenv  # Getenv pozwala nam przekazac zmienne z .env
from dotenv import load_dotenv
load_dotenv()


def setup():
    print('Tworze tabele w bazie danych')
    db = Database(getenv('DB_NAME'))  # Tworzymy obiekt Database, nazwe przekazujemy poprzez getenv
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')


def add(category: str, url: str):
    print('Dodaje nowy adres url')
    db = Database(getenv('DB_NAME'))
    db.insert('urls', None, category, url)  # wykonujemy polecenie


def fetch_categories():  # Definiujemy funkcje printujaca nam liste kategorii w bazie
    print('Lista kategorii')
    db = Database(getenv('DB_NAME'))
    categories = db.fetch_distinct('urls', 'category')

    for name in categories:
        print(name)


def index(category: str):
    db = Database(getenv('DB_NAME'))
    links = db.fetch_all('urls', category=category)

    for link in links:
        print(link[2])


if len(argv) == 2 and argv[1] == 'setup':  # Tworzymy tabele po wywołaniu polecenia setup
    setup()


if len(argv) == 4 and argv[1] == 'add':  # Dodajemy nowy zasób
    add(category=argv[2], url=argv[3])


if len(argv) == 3 and argv[1] == 'list':
    print(f'Lista linkow z kategorii: {argv[2]}')  # wyswietlamy tylko linki
    index(category=argv[2])

if len(argv) == 2 and argv[1] == 'categories':
    fetch_categories()