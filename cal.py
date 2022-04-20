class Kalkulator:
    def __init__(self):
        self.wynik = 0

    def dodawanie(self, liczba):
        self.wynik += liczba

    def odejmowanie(self, liczba):
        self.wynik -= liczba

    def mnozenie(self, liczba):
        self.wynik *= liczba

    def dzielenie(self, liczba):
        if liczba != 0:
            self.wynik /= liczba
        else:
            print('blad')


pi = 3.14
e = 2.72
kilo = 1000


