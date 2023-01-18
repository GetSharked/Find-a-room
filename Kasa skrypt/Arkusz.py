import gspread
import json
from GUI import GUI

class Arkusz:


    def Interface(self):
        self.WpiszDate(Arkusz)
        self.WpiszIlosc(Arkusz)
        self.WpiszCene(Arkusz)


    def OkreslWalute(self):
        with open('dane.json') as jsonFile:
            data = json.load(jsonFile)
            Waluty = []
            for NazwaWaluty in data["Waluty"]:
                Waluty.append(NazwaWaluty)
        return Waluty


    def WpiszDate(self):
        with open('dane.json') as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
            sa = gspread.service_account(filename="***INSERT FILE WITH GOOGLE API KEY***")
            sh = sa.open("Hajs")
            i = 2
            for Nazwa in self.OkreslWalute(Arkusz):
                print(f'WpiszDate: Wpisuje teraz date dla waluty {Nazwa}')
                wks = sh.worksheet(Nazwa)
                if wks.acell(f'A{i}').value != None:
                    i += 1
                else:
                    wks.update(f'A{i}', data["Waluty"][Nazwa]["Data"])



    def WpiszIlosc(self):
        with open('dane.json') as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
            sa = gspread.service_account(filename="***INSERT FILE WITH GOOGLE API KEY***")
            sh = sa.open("Hajs")
            i = 2
            for Nazwa in self.OkreslWalute(Arkusz):
                print(f'WpiszIlosc: Wpisuje teraz ilosc dla waluty {Nazwa}')
                wks = sh.worksheet(Nazwa)
                if wks.acell(f'B{i}').value != None:
                    i += 1
                else:
                    wks.update(f'B{i}', data["Waluty"][Nazwa]["Ilosc"])


    def WpiszCene(self):
        with open('dane.json') as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
            sa = gspread.service_account(filename="***INSERT FILE WITH GOOGLE API KEY***")
            sh = sa.open("Hajs")
            i = 2
            for Nazwa in self.OkreslWalute(Arkusz):
                print(f'WpiszCene: Wpisuje teraz cene dla waluty {Nazwa}')
                wks = sh.worksheet(Nazwa)
                if wks.acell(f'C{i}').value != None:
                    i += 1
                else:
                    wks.update(f'C{i}', data["Waluty"][Nazwa]["Cena"])

    def WpiszCeneNaTeraz(self):
        with open('dane.json') as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
            sa = gspread.service_account(filename="***INSERT FILE WITH GOOGLE API KEY***")
            sh = sa.open("Hajs")
            for Nazwa in self.OkreslWalute(Arkusz):
                print(f'WpiszCene: Wpisuje teraz cene na dzis dla waluty {Nazwa}')
                wks = sh.worksheet(Nazwa)
                wks.update('D2', data["Ceny"][Nazwa])






