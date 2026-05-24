from abc import ABC, abstractmethod

# a specifikációban megadott 3 attributum
# az árra vonatkozó egyszerű validáció került be.
# a rendszám validáció a komplexitása miatt nem kerül implementálásra
# a típus validáció a lehetséges elemek adatbázisának hiánya miatt nem kerül implementálásra.

class Auto(ABC):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int):
        self.__rendszam = rendszam
        self.__tipus = tipus
        self.__berleti_dij = berleti_dij

    # getter-ek
    @property
    def rendszam(self):
        return self.__rendszam

    @property
    def tipus(self):
        return self.__tipus

    @property
    def berleti_dij(self):
        return self.__berleti_dij

    # setter-ek
    @berleti_dij.setter
    def berleti_dij(self, uj_dij):
        if uj_dij <= 0:
            # a bérlésért fizettség járjon lehetőleg
            raise ValueError("A bérleti díjnak pozitív számnak kell lennie!")
        self.__berleti_dij = uj_dij

    @abstractmethod
    def auto_tipus(self):
        pass

    def __str__(self):
        return (
            f"Rendszám: {self.__rendszam}, "
            f"Típus: {self.__tipus}, "
            f"Bérleti díj: {self.__berleti_dij} Ft/nap"
        )