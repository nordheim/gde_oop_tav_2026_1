from auto import Auto

# az alábbi osztály megvalósítja a teherautó osztályt az Auto kiterjesztéseként
# a specifikáció nem részletezett speciális attributumokat, így azokat hasraütésszerűen vettem fel
# továbbra sem értek az autokhoz, a teherautokhoz pláne nem :)

class Teherauto(Auto):
    def __init__(
        self,
        rendszam: str,
        tipus: str,
        berleti_dij: int,
        teherbiras: int,
        rakodoterulet: float,
        uzemanyag: str
    ):
        super().__init__(rendszam, tipus, berleti_dij)

        self.__teherbiras = teherbiras
        self.__rakodoterulet = rakodoterulet

        # Üzemanyag validáció (csak benzin vagy diesel)
        if uzemanyag.lower() not in ["benzin", "diesel"]:
            raise ValueError("A teherautó üzemanyaga csak benzin vagy diesel")

        self.__uzemanyag = uzemanyag.lower()

    # Getterek
    @property
    def teherbiras(self):
        return self.__teherbiras

    @property
    def rakodoterulet(self):
        return self.__rakodoterulet

    @property
    def uzemanyag(self):
        return self.__uzemanyag

    # Setterek
    @teherbiras.setter
    def teherbiras(self, value):
        if value <= 0:
            raise ValueError("A teherbírásnak pozitívnak kell lennie!")
        self.__teherbiras = value

    @rakodoterulet.setter
    def rakodoterulet(self, value):
        if value <= 0:
            raise ValueError("A rakodóterületnek pozitívnak kell lennie!")
        self.__rakodoterulet = value

    @uzemanyag.setter
    def uzemanyag(self, value):
        if value.lower() not in ["benzin", "diesel"]:
            raise ValueError("Csak benzin vagy diesel érhető el")
        self.__uzemanyag = value.lower()

    def auto_tipus(self):
        return "Teherautó"

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Teherbírás: {self.__teherbiras} kg, "
            f"Rakodóterület: {self.__rakodoterulet} m², "
            f"Üzemanyag: {self.__uzemanyag}"
        )