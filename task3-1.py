import csv

def leggere_libri(archivo):
    """Legge un file CSV e restituisce una lista di dizionari con i dati dei libri."""
    try:
        with open(archivo, "r") as file:
            return list(csv.DictReader(file))
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

def main():
    print("\n-------------------------------------")
    libri = leggere_libri('libri.txt')

    scelta = input("Scegli il titolo del libro che vuoi acquistare: ")
    libro_scelto = cerca_scelta(scelta, libri)
    
    if not libro_scelto:
        return

    try:
        prezzo_libro = float(libro_scelto["prezzo"])
    except ValueError:
        print("Errore nel prezzo del libro.")
        return
    
    try:
        eta = int(input("Inserisci la tua età: "))
        punti = int(input("Inserisci i tuoi punti fedeltà: "))
        genere_preferito = input("Qual è il tuo genere preferito (es. Mystery, Fantasy)? ")

        prezzo_finale, percentuale_sconto = calcola_sconto(eta, punti, genere_preferito, prezzo_libro)
        
        print(f"Prezzo originale del libro: {prezzo_libro:.2f} EUR")
        print(f"Sconto applicato: {percentuale_sconto:.0f}%")
        print(f"Prezzo finale del libro: {prezzo_finale:.2f} EUR\n")
    except ValueError:
        print("Errore nell'inserimento dei dati. Assicurati di inserire valori numerici corretti.")

if __name__ == "__main__":
    main()
