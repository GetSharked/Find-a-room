from przedmiot import Notatka, Wizytowka


class Organizer:

    __wlasciciel = 'Gracjan'
    __baza = []

    def __init__(self, wlasciciel):
        self.__wlasciciel = wlasciciel

    def dodajNotatke(self):
        priorytet = input("Priorytet: ")
        tytul = input("Tytuł: ")
        tresc = input("Treść: ")

        nowa_notatka = Notatka(priorytet, tytul, tresc)
        self.__baza.append(nowa_notatka)

    def dodajWizytowke(self):
        priorytet = input("Priorytet: ")
        imie = input("Imię: ")
        nazwisko = input("Nazwisko: ")
        numer = input("Numer: ")

        nowa_wizytowka = Wizytowka(priorytet, imie, nazwisko, numer)
        self.__baza.append(nowa_wizytowka)

    def wyswietlNotatki(self):
        print('Lista notatek: ')
        for i in self.__baza:
            if i.typ == 'Notatka':
                print(i)

    def wyswietlWizytowki(self):
        print('Lista wizytowek: ')
        for i in self.__baza:
            if i.typ == 'Wizytowka':
                print(i)

