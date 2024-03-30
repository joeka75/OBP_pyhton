from abc import ABC, abstractmethod
from datetime import datetime
from datetime import timedelta


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def tipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)

    def tipus(self):
        return "Egyágyas szoba"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)

    def tipus(self):
        return "Kétágyas szoba"

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append(Foglalas(szoba, datum))
                return szoba.ar
        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True
        return False

    def listaz_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

def main():

    print("--- Hotel foglalási rendszer ---")

    szoba1 = EgyagyasSzoba("101", 10000)
    szoba2 = KetagyasSzoba("102", 15000)
    szoba3 = KetagyasSzoba("103", 20000)
    szoba4 = EgyagyasSzoba("201", 10000)
    szoba5 = KetagyasSzoba("202", 15000)
    szoba6 = KetagyasSzoba("203", 20000)

    szalloda = Szalloda("Joci Szálloda")
    szalloda.add_szoba(szoba1)
    szalloda.add_szoba(szoba2)
    szalloda.add_szoba(szoba3)
    szalloda.add_szoba(szoba4)
    szalloda.add_szoba(szoba5)
    szalloda.add_szoba(szoba6)

    szalloda.foglalas("101", datetime.now().date() + timedelta(days = 3))
    szalloda.foglalas("102", datetime.now().date() + timedelta(days = 6))
    szalloda.foglalas("103", datetime.now().date() + timedelta(days = 9))
    szalloda.foglalas("102", datetime.now().date() + timedelta(days = 2))
    szalloda.foglalas("101", datetime.now().date() + timedelta(days = 1))
    szalloda.foglalas("203", datetime.now().date() + timedelta(days = 10))
    szalloda.foglalas("202", datetime.now().date() + timedelta(days = 20))
    szalloda.foglalas("201", datetime.now().date() + timedelta(days = 15))

    while True:
        
        print("\n1. Foglalás\n2. Lemondás\n3. Foglalások listázása\n4. Kilépés")
        valasztas = input("Válassz egy műveletet: ")

        if valasztas == "1":
            szobaszam = input("Add meg a szobaszámot: ")
            datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                if datum < datetime.now():
                    print("Csak jövőbeli dátumot lehet megadni!")
                else:
                    ar = szalloda.foglalas(szobaszam, datum)
                    if ar is not None:
                        print(f"A foglalás ára: {ar} Ft")
                    else:
                        print("Nincs ilyen szobaszám.")
            except ValueError:
                print("Érvénytelen dátum formátum!")

        elif valasztas == "2":
            
           
            for i in range(len(szalloda.foglalasok)):
                if i ==0:
                    continue
                print("Foglaáls szám: " + str(i))

            foglalas_index = int(input("Add meg a lemondandó foglalás sorszámát: ")) - 1
            if 0 <= foglalas_index < len(szalloda.foglalasok):
                foglalas = szalloda.foglalasok[foglalas_index]
                if szalloda.lemondas(foglalas):
                    print("A foglalás sikeresen lemondva.")
                else:
                    print("Nem sikerült a foglalás lemondása.")
            else:
                print("Érvénytelen sorszám.")

        elif valasztas == "3":
            szalloda.listaz_foglalasok()

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
