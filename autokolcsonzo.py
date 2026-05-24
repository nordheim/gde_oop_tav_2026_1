from szemelyauto import Szemelyauto
from teherauto import Teherauto

# az autokolcsonzo osztály,
# amibe belekerül 3 előre definiált autó, amiket ki lehet kölcsönözni


class Autokolcsonzo:
    def __init__(self):
        self.__nev = "Távos kölcsönző"
        self.__autok = []

        # --- Előre feltöltött autók ---

        # 1. személyautó
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
            tipus="Limuzin",
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

    # Getter
    @property
    def nev(self):
        return self.__nev

    @property
    def autok(self):
        return self.__autok

    # Autó hozzáadás
    def auto_hozzaadas(self, auto):
        if not isinstance(auto, (Szemelyauto, Teherauto)):
            raise TypeError("Csak Személyauto vagy Teherauto adható hozzá!")
        self.__autok.append(auto)

    # Autók listázása
    def autok_listazasa(self):
        if not self.__autok:
            return "Nincs elérhető autó a rendszerben."
        return "\n".join(str(auto) for auto in self.__autok)

    # Keresés rendszám alapján
    def auto_kereses(self, rendszam: str):
        for auto in self.__autok:
            if auto.rendszam == rendszam:
                return auto
        return None

    def __str__(self):
        return f"Autókölcsönző neve: {self.__nev}, Autók száma: {len(self.__autok)}"