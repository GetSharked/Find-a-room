import sqlite3


class Database:  # Tworzymy klase bazy danych
    def __init__(self, database_name):  # łączymy się z baza za kazdym razem gdy tworzymy obiekt, przekazujemy nazwe
        self.conn = sqlite3.connect(database_name)  # Zmienna do łaczenia sie z baza
        self.cursor = self.conn.cursor()  # Cursor sluzy do wykonywania zapytan na tych dwoch wlasciwosciach

    def __del__(self):  # Potrzebujemy pozniej zakonczyc polaczenie z baza wiec uzywamy "destruktora"
        self.conn.close()  #Zamykamy połączenie, gdyz w konfiguracji baz danych jest limit polaczen
                           #i mozemy nie otrzymac dostepu do jakiegos pliku jesli nie zcommitujemy

    def create_table(self, sql: str):  # tworzymy funkcje wykonujaca rozne zapytania, podane w parametrze sql
        self.cursor.execute(sql)  # wykonanie
        self.conn.commit()  # zatwierdzenie

    def insert(self, table, *values):  # Wrzucamy do {table} wszystkie wartosci
        self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in values])})", values)
        self.conn.commit()
        # łączymy liste ze  stringiem funkcją join, lista składa sie z pytajnikow

    def fetch_all(self, table, **conditions):  # Dwie gwiazdki, bo conditions to slownik, pobieramy wartosci z kategorii
        return self.cursor.execute(
            f"SELECT * FROM {table} WHERE {' and'.join([f'{condition}=?' for condition in conditions])}",
            list(conditions.values())  # Musi byc inny typ niz dict type
        )

    def fetch_distinct(self, table, column):  # definiujemy metode wyodrebniajaca poszczegulna kolumne z tabeli
        return self.cursor.execute(
            f'SELECT DISTINCT {column} FROM {table}'
        )