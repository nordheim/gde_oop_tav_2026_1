from datetime import date


class Berles:
    def __init__(self, auto, ugyfel_nev: str, datum: str):
        self.__auto = auto
        self.__ugyfel_nev = ugyfel_nev

        try:
            self.__datum = date.fromisoformat(datum)
        except ValueError:
            raise ValueError("Hibás dátumformátum! (YYYY-MM-DD)")

        self.__ar = self.__auto.berleti_dij

    # Getterek
    @property
    def auto(self):
        return self.__auto

    @property
    def ugyfel_nev(self):
        return self.__ugyfel_nev

    @property
    def datum(self):
        return self.__datum

    @property
    def ar(self):
        return self.__ar

    def __str__(self):
        return (
            f"Ügyfél: {self.__ugyfel_nev}, "
            f"Autó: {self.__auto.rendszam}, "
            f"Dátum: {self.__datum}, "
            f"Ár: {self.__ar} Ft"
        )

    # --------------------------------------------------
    # ELŐRE DEFINIÁLT BÉRLÉSEK (NEM ÜTKÖZŐ, 3 AUTÓVAL)
    # --------------------------------------------------

    @staticmethod
    def alap_berlesek(autok):
        """
        autok: az Autokolcsonzo.autok listája
        """

        def keres(rendszam):
            for a in autok:
                if a.rendszam == rendszam:
                    return a
            raise ValueError(f"Nincs ilyen autó: {rendszam}")

        auto1 = keres("ABC-123")
        auto2 = keres("DEF-456")
        auto3 = keres("GHI-789")

        return [
            Berles(auto1, "Kiss János", "2026-05-20"),
            Berles(auto2, "Nagy Anna", "2026-05-21"),
            Berles(auto3, "Tóth Béla", "2026-05-22"),
            Berles(auto1, "Szabó Péter", "2026-05-23"),
        ]