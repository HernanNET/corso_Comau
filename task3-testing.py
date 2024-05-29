import csv
from io import StringIO

# Redefinimos la función leggere_libri para que lea desde una cadena en lugar de un archivo
def leggere_libri(archivo):
    """Legge un file CSV e restituisce una lista di dizionari con i dati dei libri."""
    try:
        return list(csv.DictReader(StringIO(archivo)))
    except FileNotFoundError:
        print("File non trovato.")
        return []

def cerca_scelta(titolo, libri):
    """Cerca un libro nella lista per titolo e lo restituisce."""
    if not titolo:
        print("Scelta non valida.")
        return None

    for libro in libri:
        if libro['titolo'].lower() == titolo.lower():
            return libro

    print("Libro non trovato.")
    return None

def calcola_sconto(eta, punti, genere_preferito, prezzo):
    """Calcola lo sconto basato su età, punti fedeltà e genere preferito."""
    sconto = 0
    
    if (eta > 60 or eta < 20) and genere_preferito.lower() == "mystery":
        sconto = 0.30
    elif 30 <= eta <= 50 or punti > 30:
        sconto = 0.15
    elif genere_preferito.lower() == "fantasy":
        sconto = 0.50
    
    prezzo_scontato = float(prezzo) * (1 - sconto)
    return prezzo_scontato, sconto * 100

# Definimos la función principal que recibe parámetros
def main(scelta, eta, punti, genere_preferito):
    print("\n-------------------------------------")
    libri_csv = """titolo,prezzo
Book1,10
Book2,20
Book3,30
Book4,40
Book5,50
Book6,60
Book7,70
Book8,80
Book9,90"""
    
    libri = leggere_libri(libri_csv)

    libro_scelto = cerca_scelta(scelta, libri)
    
    if not libro_scelto:
        return

    try:
        prezzo_libro = float(libro_scelto["prezzo"])
    except ValueError:
        print("Errore nel prezzo del libro.")
        return
    
    try:
        prezzo_finale, percentuale_sconto = calcola_sconto(eta, punti, genere_preferito, prezzo_libro)
        
        print(f"Prezzo originale del libro: {prezzo_libro:.2f} EUR")
        print(f"Sconto applicato: {percentuale_sconto:.0f}%")
        print(f"Prezzo finale del libro: {prezzo_finale:.2f} EUR\n")
    except ValueError:
        print("Errore nell'inserimento dei dati. Assicurati di inserire valori numerici corretti.")

# Función de prueba
def test_program():
    test_cases = [
        {"scelta": "Book1", "eta": 18, "punti": 10, "genere_preferito": "Mystery"},
        {"scelta": "Book2", "eta": 31, "punti": 30, "genere_preferito": "Mystery"},
        {"scelta": "Book3", "eta": 31, "punti": 30, "genere_preferito": "Fantasy"},
        {"scelta": "Book4", "eta": 65, "punti": 40, "genere_preferito": "Romance"},
        {"scelta": "Book5", "eta": 25, "punti": 35, "genere_preferito": "Fantasy"},
        {"scelta": "Book6", "eta": 45, "punti": 20, "genere_preferito": "Mystery"},
        {"scelta": "Book7", "eta": 19, "punti": 5, "genere_preferito": "Science Fiction"},
        {"scelta": "Book8", "eta": 55, "punti": 50, "genere_preferito": "Fantasy"},
        {"scelta": "Book9", "eta": 70, "punti": 10, "genere_preferito": "Mystery"},
    ]

    for case in test_cases:
        print(f"Testing case: {case}")
        main(case["scelta"], case["eta"], case["punti"], case["genere_preferito"])

if __name__ == "__main__":
    test_program()
