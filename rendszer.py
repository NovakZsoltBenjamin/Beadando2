from legitarsasag import LegiTarsasag
from jarat import BelfoldiJarat, NemzetkoziJarat
from jegyfoglalas import JegyFoglalas, JegyFoglalasBuilder
from datetime import datetime

class FoglalasiRendszer:
    def __init__(self):
        self.legitarsasag = LegiTarsasag("DemoAir")
        self.foglalasok = []
        self._elore_betoltott_adatok()

    def _elore_betoltott_adatok(self):
        j1 = BelfoldiJarat("B101", "Budapest", 15000)
        j2 = NemzetkoziJarat("N201", "London", 45000)
        j3 = NemzetkoziJarat("N202", "Berlin", 40000)
        self.legitarsasag.jarat_hozzaad(j1)
        self.legitarsasag.jarat_hozzaad(j2)
        self.legitarsasag.jarat_hozzaad(j3)

        builder = JegyFoglalasBuilder()
        self.foglalasok.append(builder.set_utas_nev("Kiss Anna").set_jarat(j1).set_datum("2025-06-20").build())
        self.foglalasok.append(builder.set_utas_nev("Nagy Béla").set_jarat(j2).set_datum("2025-06-22").build())
        self.foglalasok.append(builder.set_utas_nev("Tóth Zsuzsa").set_jarat(j3).set_datum("2025-07-01").build())
        self.foglalasok.append(builder.set_utas_nev("Varga Péter").set_jarat(j1).set_datum("2025-06-25").build())
        self.foglalasok.append(builder.set_utas_nev("Szabó Mária").set_jarat(j2).set_datum("2025-06-28").build())
        self.foglalasok.append(builder.set_utas_nev("Farkas Imre").set_jarat(j3).set_datum("2025-07-05").build())

    def jegy_foglalasa(self, utas_nev, jaratszam, datum):
        jarat = self.legitarsasag.jarat_keres(jaratszam)
        if jarat is None:
            return "Nincs ilyen járat."
        if not self._ervenyes_datum(datum):
            return "Érvénytelen dátum."
        builder = JegyFoglalasBuilder()
        foglalas = builder.set_utas_nev(utas_nev).set_jarat(jarat).set_datum(datum).build()
        self.foglalasok.append(foglalas)
        return f"Sikeres foglalás! Ár: {jarat.jegyar} Ft"

    def foglalas_lemondasa(self, utas_nev, jaratszam, datum):
        for f in self.foglalasok:
            if f.utas_nev == utas_nev and f.jarat.jaratszam == jaratszam and f.datum == datum:
                self.foglalasok.remove(f)
                return "Foglalás sikeresen lemondva."
        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        return [f.informacio() for f in self.foglalasok]

    def _ervenyes_datum(self, datum):
        try:
            datum_obj = datetime.strptime(datum, "%Y-%m-%d")
            return datum_obj > datetime.now()
        except ValueError:
            return False