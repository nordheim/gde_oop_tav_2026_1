from auto import Auto

# a specifikáció szerint tartalmaznia kel la személyautókra vonatkozó speciális attributumait.
# a korábbi minta kódokban erre nem sok utalást találtam ->
# a saját kútfőmből próbáltam meg, de nem értek az autókhoz egyáltalán.


class Szemelyauto(Auto):
    def __init__(
        self,
        rendszam: str,
        tipus: str,
        berleti_dij: int,
        utasszam: int,
        csomagter: int,
        valto_tipus: str,
        uzemanyagok: list,
        hibrid: bool = False
    ):
        super().__init__(rendszam, tipus, berleti_dij)

        self.__utasszam = utasszam
        self.__csomagter = csomagter

        # Váltó validáció
        if valto_tipus.lower() not in ["automata", "manualis"]:
            raise ValueError("A vátló nem lehet csak automata vagy manuális")

        self.__valto_tipus = valto_tipus.lower()

        # Üzemanyag validáció (lista)
        if not isinstance(uzemanyagok, list) or len(uzemanyagok) == 0:
            raise ValueError("Nincs megadva üzemanyag!")

        ervenyes = {"benzin", "diesel", "elektromos"}

        normalizalt = []
        for u in uzemanyagok:
            u = u.lower()
            if u not in ervenyes:
                raise ValueError(f"Érvénytelen üzemanyag: {u}")
            normalizalt.append(u)

        self.__uzemanyagok = list(set(normalizalt))  # duplumok kiszűrése

        # Hibrid validáció
        if not isinstance(hibrid, bool):
            raise ValueError("A hibrid csak True vagy False lehet!")

        # Hibrid + manuális tiltás
        if hibrid and valto_tipus.lower() == "manualis":
            raise ValueError("Hibrid autó nem lehet manuális váltós!")

        self.__hibrid = hibrid

    @property
    def utasszam(self):
        return self.__utasszam

    @property
    def csomagter(self):
        return self.__csomagter

    @property
    def valto_tipus(self):
        return self.__valto_tipus

    @property
    def uzemanyagok(self):
        return self.__uzemanyagok

    @property
    def hibrid(self):
        return self.__hibrid

    # a setter-ek
    @utasszam.setter
    def utasszam(self, value):
        if value <= 0:
            raise ValueError("Utasszámnak csak pozitív lehet")
        self.__utasszam = value

    @csomagter.setter
    def csomagter(self, value):
        if value < 0:
            raise ValueError("Csomagtér csak pozitív lehet")
        self.__csomagter = value

    @valto_tipus.setter
    def valto_tipus(self, value):
        value = value.lower()
        if value not in ["automata", "manualis"]:
            raise ValueError("A váltó csak automata vagy manualis lehet")

        if self.__hibrid and value == "manualis":
            raise ValueError("Hibrid autó nem lehet manuális váltós")

        self.__valto_tipus = value

    @uzemanyagok.setter
    def uzemanyagok(self, value):
        if not isinstance(value, list) or len(value) == 0:
            raise ValueError("Az üzemanyag típusa nem lehet üres")

        ervenyes = {"benzin", "diesel", "elektromos"}
        normalizalt = []

        for u in value:
            u = u.lower()
            if u not in ervenyes:
                raise ValueError(f"Érvénytelen üzemanyag: {u}")
            normalizalt.append(u)

        normalizalt = list(set(normalizalt))

    @hibrid.setter
    def hibrid(self, value):
        if not isinstance(value, bool):
            raise ValueError("A hibrid csak True/False lehet!")

        if value and self.__valto_tipus == "manualis":
            raise ValueError("Hibrid autó nem lehet manuális váltós!")

        self.__hibrid = value

    def auto_tipus(self):
        return "Személyautó"

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Utasszám: {self.__utasszam}, "
            f"Csomagtér: {self.__csomagter} liter, "
            f"Váltó: {self.__valto_tipus}, "
            f"Üzemanyagok: {', '.join(self.__uzemanyagok)}, "
            f"Hibrid: {self.__hibrid}"
        )