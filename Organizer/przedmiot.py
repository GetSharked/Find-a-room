from abc import ABC, abstractmethod


class Przedmiot(ABC):
    def __init__(self, typ, priorytet):
        self.typ = typ
        self.priorytet = priorytet

    @abstractmethod
    def __str__(self):
        pass

class Notatka(Przedmiot):
    def __init__(self, priorytet, tytul, tresc):
        super().__init__('Notatka', priorytet)
        self.tytul = tytul
        self.tresc = tresc

    def __str__(self):
        info = "Priorytet" + self.priorytet + '\n'
        info += self.tytul + "\n"
        info += self.tresc
        return info

class Wizytowka(Przedmiot):
    def __init__(self, priorytet, imie, nazwisko, numer):
        super().__init__('Wizytówka', priorytet)
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def __str__(self):
        info = "Priorytet: " + self.priorytet +  '\n'
        info += self.imie + " " + self.nazwisko + "\n"
        info += self.numer
        return info