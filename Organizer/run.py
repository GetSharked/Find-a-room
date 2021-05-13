from organizer import Organizer


while True:

    print("""Co chcialbys wykonac?
                1.Dodaj notatke
                2.Dodaj wizytowke
                3.Wyswietl notatki
                4.Wyswietl wizytowki
                0.Zamknij programe 
         """)

    x = input()

    if x == '0': break
    if x == '1': Organizer.dodajNotatke(Organizer)
    if x == '2': Organizer.dodajWizytowke(Organizer)
    if x == '3': Organizer.wyswietlNotatki(Organizer)
    if x == '4': Organizer.wyswietlWizytowki(Organizer)