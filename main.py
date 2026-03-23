import shutil
from pathlib import Path

#Estrae da ogni file la sua estensione, in minuscolo e senza punto, se non ha estensione
#restituisce "senza_estensione"
def estrai_estensione(file: Path) -> str:
    estensione = file.suffix
    return estensione[1:].lower() if estensione else "senza_estensione"

#Crea la sottocartella (se non esiste) e sposta il file
def crea_muovi_in_cartella(file: Path, cartella_base: Path, estensione: str) -> None:
    cartella_destinazione = cartella_base / estensione
    cartella_destinazione.mkdir(exist_ok=True)
    try:
        shutil.move(file, cartella_destinazione)
        print(f"{file.name} SPOSTATO IN /{estensione}") 
    except Exception as error:
        print(f"ERRORE CON '{file.name}': {error}")

#Organizza i file nelle sottocartelle per estensione
def organizza_download() -> None:
    percorso = Path.home() / "Downloads"
    file_lista = [f for f in percorso.iterdir() if f.is_file()]
    print(f"NUMERO FILE TROVATI: {len(file_lista)}")

    for file in file_lista:    
        estensione = estrai_estensione(file)
        crea_muovi_in_cartella(file, percorso, estensione)

if __name__ == "__main__":
    organizza_download()            