import requests

# Potrzebujemy przeliczyć trochę waluty, czasy niepewne,
# warto mieć na uwadze swoją ulubioną walutę.
# Napisz klasę, która będzie zawierać dwie metody:

#       przeliczenie wybranej waluty z tabeli A na złotówki  <- dane wejściowe: kod waluty, ilość waluty
#       wskazanie aktualnego kursu z tabeli A <- dane wjećiowe: kod waluty

# Klasa w celu przeliczenia waluty powinna skorzystać z aktualnych kursów z Narodowego Banku Polskiego
# dokumentację API dla NBP znajdziesz pod adresem http://api.nbp.pl/

# Gdy skończysz prześlij mi swoje zadanie w postaci linku do swojego GitHuba, innych linków nie przyjmuję :)
# Na rozwiązanie czekam do końca dnia do niedzieli 22.01.2023


class Waluty:

    __url = 'https://api.nbp.pl/api/exchangerates/tables/a/today/?format=json'

    def przeliczenie(self, kod_waluty, ilosc_waluty):
        data = requests.get(self.__url)
        data = data.json()

        for x in data[0]['rates']:
            if kod_waluty == x['code']:
                return ilosc_waluty*float(x['mid'])

    def wskazanie(self, kod_waluty):
        data = requests.get(self.__url)
        data = data.json()

        for x in data[0]['rates']:
            if kod_waluty == x['code']:
                return x['mid']



