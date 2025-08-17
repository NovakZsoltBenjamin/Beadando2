from rendszer import FoglalasiRendszer

def menu():
    print("\nRepülőjegy Foglalási Rendszer")
    print("1. Jegy foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Járatok listázása")
    print("0. Kilépés")

def jegy_foglalasa_func(rendszer):
    utas_nev = input("Add meg az utas nevét: ")
    jaratszam = input("Add meg a járatszámot: ")
    datum = input("Add meg az utazás dátumát (YYYY-MM-DD): ")
    eredmeny = rendszer.jegy_foglalasa(utas_nev, jaratszam, datum)
    print(eredmeny)

def foglalas_lemondasa_func(rendszer):
    utas_nev = input("Add meg az utas nevét: ")
    jaratszam = input("Add meg a járatszámot: ")
    datum = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")
    eredmeny = rendszer.foglalas_lemondasa(utas_nev, jaratszam, datum)
    print(eredmeny)

def foglalasok_listazasa_func(rendszer):
    print("\nAktuális foglalások:")
    for f in rendszer.foglalasok_listazasa():
        print(f)

def jaratok_listazasa_func(rendszer):
    print("\nElérhető járatok:")
    for j in rendszer.legitarsasag.listaz_jaratok():
        print(j)

def main():
    rendszer = FoglalasiRendszer()
    actions = {
        "1": lambda: jegy_foglalasa_func(rendszer),
        "2": lambda: foglalas_lemondasa_func(rendszer),
        "3": lambda: foglalasok_listazasa_func(rendszer),
        "4": lambda: jaratok_listazasa_func(rendszer),
    }
    while True:
        menu()
        valaszt = input("Válassz egy műveletet: ")
        if valaszt == "0":
            print("Kilépés...")
            break
        elif valaszt in actions:
            actions[valaszt]()
        else:
            print("Érvénytelen választás, próbáld újra!")

if __name__ == "__main__":
    main()