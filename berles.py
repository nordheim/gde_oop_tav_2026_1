from datetime import date


class Berles:
    __berlesek = []
    __init_done = False

    def __init__(self, auto, ugyfel_nev: str, datum: str):
        self.__auto = auto
        self.__ugyfel_nev = ugyfel_nev

        try:
            self.__datum = date.fromisoformat(datum)
        except ValueError:
            raise ValueError("Hibás dátumformátum! (YYYY-MM-DD)")

        self.__ar = self.__auto.berleti_dij

    # ------------------------
    # GETTEREK
    # ------------------------
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

    # ------------------------
    # ÜTKÖZÉS KONTROLL
    # ------------------------
    @classmethod
    def auto_foglalt_e(cls, auto, datum: str):
        datum = date.fromisoformat(datum)

        for b in cls.__berlesek:
            if b.auto == auto and b.datum == datum:
                return True
        return False

    # ------------------------
    # BÉRLÉS LÉTREHOZÁS
    # ------------------------
    @classmethod
    def letrehoz(cls, auto, ugyfel_nev: str, datum: str):
        if cls.auto_foglalt_e(auto, datum):
            raise ValueError("Az autó ezen a napon már foglalt!")

        uj = Berles(auto, ugyfel_nev, datum)
        cls.__berlesek.append(uj)
        return uj

    # ------------------------
    # LEMONDÁS
    # ------------------------
    @classmethod
    def lemond(cls, auto, datum: str):
        datum = date.fromisoformat(datum)

        for b in cls.__berlesek:
            if b.auto == auto and b.datum == datum:
                cls.__berlesek.remove(b)
                return True

        raise ValueError("Nem található ilyen bérlés!")

    # ------------------------
    # LISTÁZÁS
    # ------------------------
    @classmethod
    def osszes(cls):
        return cls.__berlesek

    # ------------------------
    # ELŐRE DEFINIÁLT BÉRLÉSEK
    # ------------------------
    @classmethod
    def init_alap_berlesek(cls, autok):
        if cls.__init_done:
            return

        def keres(rsz):
            for a in autok:
                if a.rendszam == rsz:
                    return a
            raise ValueError(f"Nincs ilyen autó: {rsz}")

        auto1 = keres("ABC-123")
        auto2 = keres("DEF-456")
        auto3 = keres("GHI-789")

        cls.__berlesek.extend([
            Berles(auto1, "Kiss János", "2026-05-20"),
            Berles(auto2, "Nagy Anna", "2026-05-21"),
            Berles(auto3, "Tóth Béla", "2026-05-22"),
            Berles(auto1, "Szabó Péter", "2026-05-23"),
        ])

        cls.__init_done = True

    # ------------------------
    # STRING
    # ------------------------
    def __str__(self):
        return (
            f"Ügyfél: {self.__ugyfel_nev}, "
            f"Autó: {self.__auto.rendszam}, "
            f"Dátum: {self.__datum}, "
            f"Ár: {self.__ar} Ft"
        )