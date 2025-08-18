from jarat import BelfoldiJarat, NemzetkoziJarat

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaad(self, jarat):
        self.jaratok.append(jarat)

    def jarat_keres(self, jaratszam):
        for j in self.jaratok:
            if j.jaratszam == jaratszam:
                return j
        return None

    def listaz_jaratok(self):
        return [j.informacio() for j in self.jaratok]