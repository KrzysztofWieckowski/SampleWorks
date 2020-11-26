# Tworzenie nowej listy włg podanej liczby elementów.

# Do obiektu nowa_lista w części MAIN wpisz:
# - dowolną listę ("lista");
# - dowolną liczbę elementów ("liczba"). Podawana liczba elementów musi być >=0.


class Nowa_lista(object):

    def __init__(self, stara_lista, liczba):
        self.stara_lista = stara_lista
        self.liczba = liczba

    def tworzenie_nowej_listy(self):
        x = len(self.stara_lista)
        y = self.liczba

        if x > y:
            ile_elementow_odjac = x - y
            ile_elementów_zostaje = x - ile_elementow_odjac
            nowa_l = self.stara_lista[0:ile_elementów_zostaje]
            print(nowa_l)

        if x == y:
            print(self.stara_lista)

        if x < y:
            iloraz = int(y/x + 1)
            lista_pomocnicza = self.stara_lista * iloraz
            ile_elementow_dodac = y - x
            lista_do_dodania = lista_pomocnicza[:ile_elementow_dodac]
            for i in range(ile_elementow_dodac):
                    z = lista_do_dodania[i]
                    self.stara_lista.append(z)
            print(self.stara_lista)


# MAIN
nowa_lista = Nowa_lista(["k", "l", "m", "n"], 8)
wynik = nowa_lista.tworzenie_nowej_listy()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.") 
