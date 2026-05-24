from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles


class Autokolcsonzo:
    def __init__(self):
        self.__nev = "Távos kölcsönző"
        self.__autok = []

        # ------------------------
        # ALAP AUTÓK
        # ------------------------

        auto1 = Szemelyauto(
            rendszam="ABC-123",
            tipus="Sedan",
            berleti_dij=15000,
            utasszam=5,
            csomagter=450,
            valto_tipus="automata",
            uzemanyagok=["benzin", "elektromos"],
            hibrid=True
        )

        auto2 = Szemelyauto(
            rendszam="DEF-456",
            tipus="Hatchback",
            berleti_dij=12000,
            utasszam=4,
            csomagter=300,
            valto_tipus="manualis",
            uzemanyagok=["benzin"],
            hibrid=False
        )

        auto3 = Teherauto(
            rendszam="GHI-789",
            tipus="Furgon",
            berleti_dij=25000,
            teherbiras=3500,
            rakodoterulet=12.5,
            uzemanyag="diesel"
        )

        self.__autok.extend([auto1, auto2, auto3])

        # ------------------------
        # ALAP BÉRLÉSEK BETÖLTÉSE
        # ------------------------
        Berles.init_alap_berlesek(self.__autok)

    # ------------------------
    # AUTÓ KEZELÉS
    # ------------------------

    @property
    def nev(self):
        return self.__nev

    @property
    def autok(self):
        return self.__autok

    def auto_kereses(self, rendszam: str):
        for auto in self.__autok:
            if auto.rendszam == rendszam:
                return auto
        return None

    def auto_hozzaadas(self, auto):
        if not isinstance(auto, (Szemelyauto, Teherauto)):
            raise TypeError("Csak Szemelyauto vagy Teherauto adható hozzá!")
        self.__autok.append(auto)

    def autok_listazasa(self):
        if not self.__autok:
            return "Nincs elérhető autó."
        return "\n".join(str(a) for a in self.__autok)

    # ------------------------
    # BÉRLÉS LOGIKA (DELEGÁLÁS)
    # ------------------------

    def auto_berles(self, rendszam: str, ugyfel_nev: str, datum: str):
        auto = self.auto_kereses(rendszam)

        if not auto:
            raise ValueError("Nem létező rendszám!")

        return Berles.letrehoz(auto, ugyfel_nev, datum)

    def berles_lemondas(self, rendszam: str, datum: str):
        auto = self.auto_kereses(rendszam)

        if not auto:
            raise ValueError("Nem létező rendszám!")

        return Berles.lemond(auto, datum)

    def aktiv_berlesek(self):
        berlesek = Berles.osszes()

        if not berlesek:
            return "Nincs aktív bérlés."

        return "\n".join(str(b) for b in berlesek)

    # ------------------------
    # STRING
    # ------------------------
    def __str__(self):
        return (
            f"Autókölcsönző neve: {self.__nev}, "
            f"Autók száma: {len(self.__autok)}"
        )