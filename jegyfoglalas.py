class JegyFoglalas:
    def __init__(self, utas_nev, jarat, datum):
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.datum = datum

    def informacio(self):
        return f"{self.utas_nev} - {self.jarat.jaratszam} ({self.jarat.celallomas}) - {self.datum} - {self.jarat.jegyar} Ft"

class JegyFoglalasBuilder:
    def __init__(self):
        self._utas_nev = None
        self._jarat = None
        self._datum = None

    def set_utas_nev(self, utas_nev):
        self._utas_nev = utas_nev
        return self

    def set_jarat(self, jarat):
        self._jarat = jarat
        return self

    def set_datum(self, datum):
        self._datum = datum
        return self

    def build(self):
        if self._utas_nev is None or self._jarat is None or self._datum is None:
            raise ValueError("Hiányzó adatok a foglaláshoz.")
        return JegyFoglalas(self._utas_nev, self._jarat, self._datum)