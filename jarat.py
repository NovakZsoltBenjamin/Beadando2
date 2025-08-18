from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def informacio(self):
        pass

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def informacio(self):
        return f"Belföldi járat: {self.jaratszam}, Cél: {self.celallomas}, Ár: {self.jegyar} Ft"

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def informacio(self):
        return f"Nemzetközi járat: {self.jaratszam}, Cél: {self.celallomas}, Ár: {self.jegyar} Ft"