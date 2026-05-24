from autokolcsonzo import Autokolcsonzo
from datetime import date


def menu():
    print("\n===== AUTÓKÖLCSÖNZŐ RENDSZER =====")
    print("1. Autók listázása")
    print("2. Autó bérlése")
    print("3. Bérlés lemondása")
    print("4. Aktív bérlések listázása")
    print("0. Kilépés")
    print("===================================")


def datum_ellenoriz(datum_str: str):
    try:
        date.fromisoformat(datum_str)
        return True
    except ValueError:
        return False


def main():
    kolcsonzo = Autokolcsonzo()

    while True:
        menu()
        valasztas = input("Válassz egy opciót: ")

        # -------------------------
        # 1. AUTÓK LISTÁZÁSA
        # -------------------------
        if valasztas == "1":
            print("\n--- Elérhető autók ---")
            print(kolcsonzo.autok_listazasa())

        # -------------------------
        # 2. BÉRLÉS
        # -------------------------
        elif valasztas == "2":
            rendszam = input("Add meg a rendszámot: ")
            nev = input("Add meg a neved: ")
            datum = input("Add meg a dátumot (YYYY-MM-DD): ")

            if not datum_ellenoriz(datum):
                print("Hibás dátum! Helyes formátum: YYYY-MM-DD")
                continue

            try:
                berles = kolcsonzo.auto_berles(rendszam, nev, datum)
                print("\nSikeres bérlés!")
                print(berles)
            except Exception as e:
                print(f"Hiba: {e}")

        # -------------------------
        # 3. LEMONDÁS
        # -------------------------
        elif valasztas == "3":
            rendszam = input("Add meg a rendszámot: ")
            datum = input("Add meg a dátumot (YYYY-MM-DD): ")

            if not datum_ellenoriz(datum):
                print("Hibás dátum! Helyes formátum: YYYY-MM-DD")
                continue

            try:
                uzenet = kolcsonzo.berles_lemondas(rendszam, datum)
                print("Bérlés sikeresen lemondva!")
            except Exception as e:
                print(f"Hiba: {e}")

        # -------------------------
        # 4. AKTÍV BÉRLÉSEK
        # -------------------------
        elif valasztas == "4":
            print("\n--- Aktív bérlések ---")
            print(kolcsonzo.aktiv_berlesek())

        # -------------------------
        # 0. KILÉPÉS
        # -------------------------
        elif valasztas == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")


if __name__ == "__main__":
    main()