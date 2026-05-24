from autokolcsonzo import Autokolcsonzo
from berles import Berles


def menu():
    print("\n===== AUTÓKÖLCSÖNZŐ RENDSZER =====")
    print("1. Autók listázása")
    print("2. Autó bérlése")
    print("3. Bérlés lemondása")
    print("4. Aktív bérlések listázása")
    print("0. Kilépés")
    print("===================================")


def main():
    kolcsonzo = Autokolcsonzo()

    # --- előre feltöltött bérlések ---
    # (ha a Berles alap_berlesek-t akarod használni)
    # kolcsonzo.betolt_berlesek(Berles.alap_berlesek(kolcsonzo.autok))

    while True:
        menu()
        valasztas = input("Válassz egy opciót: ")

        try:
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

                berles = kolcsonzo.auto_berles(rendszam, nev, datum)
                print("\nSikeres bérlés!")
                print(berles)

            # -------------------------
            # 3. LEMONDÁS
            # -------------------------
            elif valasztas == "3":
                rendszam = input("Add meg a rendszámot: ")
                datum = input("Add meg a dátumot (YYYY-MM-DD): ")

                uzenet = kolcsonzo.berles_lemondas(rendszam, datum)
                print(uzenet)

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
                print("nincs ilyen2 választás!")

        except Exception as e:
            print(f"Hiba: {e}")


if __name__ == "__main__":
    main()