import sys
from PySide2 import QtCore, QtWidgets, QtGui


class InLineTranslation():
    def __init__(self, to_translate, input_form, translated, correct_translation):
        self.to_translate = to_translate  # wyswietlony klucz
        self.input_form = input_form  # pole
        self.translated = translated  # pobrana wartosc
        self.correct_translation = correct_translation  #poprawna wartosc


class AppWidget(QtWidgets.QWidget):  # Dziedziczymy
    def __init__(self, words):  # Odbieramy słownik w inicie
        super().__init__()  # Pozwoli cos dodac bez nadpisania tego w klasie dziedziczonej
        self.points = 0  # punkty za poprawne odpowiedzi
        self.words = words  # tworzymy wlasciwosc bo chcemy uzyc slownika w initialize_layout
        self.state = []  # lista, w której bedziemy przechowywac przesłane słówka
        self.layout = self.initialize_layout()
        self.setLayout(self.layout)  # Ustawienie komponentu

    def on_submit(self):  # zdarzenie po nacisnieciu submita
        self.points = 0
        for inline in self.state:
            if inline.correct_translation == inline.input_form.text():  # sprawdzamy czy sie zgadza
                self.points += 1

        msg = QtWidgets.QMessageBox()  # Tworzymy alert
        msg.setText(f'Zdobywasz {self.points} punktów!')  # Ustawiamy tekst w alercie
        msg.exec()

    def initialize_layout(self):  # zwracamy layout z tej metody
        row = 0
        grid = QtWidgets.QGridLayout()  # Dodajemy kolumny na osi wspolrzednych (0,0) - lewy gorny rog
        for key, correct_translation in self.words.items():  # dostep do wartosci to items()
            to_translate = QtWidgets.QLabel(key)  # Label wyswietla nam tekst na stronie
            input_form = QtWidgets.QLineEdit()   # Pole do wpisania
            self.state.append(InLineTranslation(key, input_form, '', correct_translation))  # Przekazujemy do listy

            grid.addWidget(to_translate, row, 0)  # pozycjonujemy słówko do przetlumaczenia
            grid.addWidget(input_form, row, 1)  # pozycjonujemy pole na tłumaczenie
            row += 1

        submit = QtWidgets.QPushButton('Sprawdź')  # tworzenie przycisku submit
        submit.clicked.connect(self.on_submit)  # dodanie metody do submita, przypiecie zdarzenia
        grid.addWidget(submit, row, 1)  # pozycja przycisku

        return grid






if __name__ == '__main__':
    words = {
        'et hunt': 'pies'
    }
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('Nauka słówek z norweskiego by Gracjan')  # Tytuł aplikacji
    appWidget = AppWidget(words)  # wrzucamy słownik do widgetu
    appWidget.resize(200, 200)  # Rozmiar okna
    appWidget.show()  # Pokazujemy widgeta na ekranie
    sys.exit(app.exec_())
