from database import Database
from sys import argv
from os import getenv  # Getenv pozwala nam przekazac zmienne z .env
from dotenv import load_dotenv
load_dotenv()

if len(argv) == 2 and argv[1] == 'setup':  # Tworzymy tabele po wywołaniu polecenia setup
    print('Tworze tabele w bazie danych')
    db = Database(getenv('DB_NAME'))  # Tworzymy obiekt Database, nazwe przekazujemy poprzez getenv
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')


if len(argv) == 4 and argv[1] == 'add':  # Dodajemy nowy zasób
    print('Dodaje nowy adres url')
    category = argv[2]
    url = argv[3]
    db = Database(getenv('DB_NAME'))
    db.insert('urls', None, category, url)  # wykonujemy polecenie


if len(argv) == 3 and argv[1] == 'list':
    print(f'Lista linkow z kategorii: {argv[2]}')  # wyswietlamy tylko linki
    category = argv[2]
    db = Database(getenv('DB_NAME'))
    links = db.fetch_all('urls', category=category)

    for link in links:
        print(link[2])