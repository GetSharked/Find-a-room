import json
import requests
from bs4 import BeautifulSoup
from requests import get
import datetime


class GUI:

    def Interfejs(self):
        while True:
            print('APKA DO DYSPONOWANIA OSZCZEDNOSCIAMI')
            term = int(input("""Wybierz co chcesz zrobić:
1. Wyswietl dane:
2. Sprawdz aktualne ceny:
3. Rozdysponuj pieniadze
4. Zanotuj kupione krypto
0. Zakończ\n"""))
            match term:
                case 1:
                    self.WyswietlDane(GUI)
                    tik = str(input("Czy chcesz zmienic proporcje? (Y/N)"))
                    if tik == 'Y' or tik == 'y':
                        self.ZmienProporcje(GUI)
                    else:
                        self.Interfejs(GUI)
                case 2:
                    self.ParsowanieCenZeStrony(GUI)
                case 3:
                    self.Rozdysponuj(GUI)
                case 4:
                    self.Zanotuj(GUI)
                case 0:
                    return False

    def WyswietlDane(self):
        with open('dane.json') as jsonFile:
            data = json.load(jsonFile)
            print(f'############   Proporcje   ############')
            for nazwa, wartosci in data['Proporcje'].items():
                print(nazwa, wartosci)
            print('\nWALUTY\n')
            for nazwa, wartosci in data['Waluty'].items():
                print(f'############   {nazwa}   ############')
                for dane in wartosci.items():
                    print(f"{dane[0]}: {dane[1]}")
            jsonFile.close()

    def ZmienProporcje(self):
        with open('dane.json', "r+") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
            for x, y in data['Proporcje'].items():
                print(x + ': ')
                data['Proporcje'][x] = float(input())
            print("Proporcje: ")
            for x, y in data['Proporcje'].items():
                print(x, y)
            jsonFile = open("dane.json", "w+")
            jsonFile.write(json.dumps(data))
            jsonFile.close()

    def Rozdysponuj(self):
        dane = open('dane.json')
        data = json.load(dane)
        cash = int(input('Podaj ilosc gotowki: '))
        for x, y in data['Proporcje'].items():
            print(x, cash*y)

    def ParsowanieCenZeStrony(self):
        with open('dane.json', "r+") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        krypto = ['BTCUSDT', 'BNBUSDT', 'ETHUSDT', 'XRPUSDT']
        Normalne_waluty = ['euro', 'funta']
        for Nazwa in Normalne_waluty:
            URL = f'https://internetowykantor.pl/kurs-{Nazwa}/'
            page = get(f'{URL}')
            bs = BeautifulSoup(page.content, 'html.parser')
            kurs = bs.find('span', class_='bem-single-rate-box__item-rate').get_text().strip()
            print(f'Cena {Nazwa} wynosi {kurs}')
            if Nazwa == 'euro':
                Nazwa = 'Euro'
                data["Ceny"][Nazwa] = kurs
            elif Nazwa == 'funta':
                Nazwa = 'Funty'
                data["Ceny"][Nazwa] = kurs
        for waluta in krypto:
            URL = f"https://api.binance.com/api/v3/ticker/price?symbol={waluta}"
            data2 = requests.get(URL)
            data2 = data2.json()
            print(f"Cena {data2['symbol']} wynosi {round(float(data2['price']), 4)}")
            if waluta == 'BTCUSDT':
                waluta = 'BTC'
                data["Ceny"][waluta] = round(float(data2['price']), 4)
            elif waluta == 'BNBUSDT':
                waluta = 'BNB'
                data["Ceny"][waluta] = round(float(data2['price']), 4)
            elif waluta == 'ETHUSDT':
                waluta = 'ETH'
                data["Ceny"][waluta] = round(float(data2['price']), 4)
            elif waluta == 'XRPUSDT':
                waluta = 'XRP'
                data["Ceny"][waluta] = round(float(data2['price']), 4)
        print("\n\n")
        jsonFile = open("dane.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()

    def Zanotuj(self):
        # Waluta = [cena, ilosc, data]
        with open('dane.json', "r+") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        for nazwa in data["Waluty"]:
            data["Waluty"][nazwa]["Cena"] = float(input(f"Za jaką cenę kupiłeś {nazwa}?"))
            data["Waluty"][nazwa]["Ilosc"] = float(input(f"Jaka ilosc {nazwa}?"))
            data["Waluty"][nazwa]["Data"] = datetime.date.today()

        jsonFile = open("dane.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()






