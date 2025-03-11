import random

# Definice filmů
film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}

film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}

film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}

# Funkce na sjednocení filmů do jednoho slovníku
def sjednot_filmy(*seznam_filmu):
    filmy = {}
    for film in seznam_filmu:
        jmeno = film["jmeno"]
        filmy[jmeno] = {k: v for k, v in film.items() if k != "jmeno"}
    return filmy

# Sjednocení filmů do jednoho slovníku
filmy = sjednot_filmy(film_1, film_2, film_3)

# Funkce pro zobrazení hlavního menu
def zobraz_uvod():
    uvod = """
               VÍTEJ V NAŠEM FILMOVÉM SLOVNÍKU!               
==============================================================
 1) dostupné filmy | 2) detaily filmu | 3) doporuč film | 4) seznam režisérů
==============================================================
    """
    print(uvod)

# Funkce pro zobrazení seznamu filmů
def zobraz_filmy():
    seznam_filmu = ", ".join(filmy.keys())
    print(f"""
                       Dostupné filmy:                        
==============================================================
{seznam_filmu}
==============================================================
""")

# Funkce pro zobrazení detailů filmu
def zobraz_detaily():
    nazev = input("\nZadej název filmu: ")
    if nazev in filmy:
        print(f"\nDetaily filmu '{nazev}':")
        for k, v in filmy[nazev].items():
            print(f"{k.capitalize()}: {v}")
    else:
        print("Film nebyl nalezen.")

# Funkce pro doporučení náhodného filmu
def doporuc_film():
    doporuceny = random.choice(list(filmy.keys()))
    print(f"\nDoporučujeme ti film: {doporuceny}")

# Funkce pro zobrazení všech režisérů
def zobraz_rezisery():
    reziseri = {film["reziser"] for film in filmy.values()}  # Množina unikátních režisérů
    seznam_reziseru = ", ".join(reziseri)  # Seznam režisérů jako text
    print(f"""
Všichni režiséři:
==============================================================
{seznam_reziseru}
==============================================================
""")

# Hlavní program
while True:
    zobraz_uvod()  # Zobrazení menu
    volba = input("Vyber možnost (1-4, nebo 'q' pro ukončení): ")
    
    if volba == "1":
        zobraz_filmy()
    elif volba == "2":
        zobraz_detaily()
    elif volba == "3":
        doporuc_film()
    elif volba == "4":
        zobraz_rezisery()  # Zobrazení režisérů
    elif volba.lower() == "q":
        print("Děkujeme za použití filmového slovníku. Měj se!")
        break
    else:
        print("Neplatná volba, zkus to znovu.")
