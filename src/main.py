# Inizio del file: Nome, Cognome, Matricola

from assembler import Assembler
from lmc import LMC
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 src/main.py <percorso_file_assembly>")
        return

    assembly_file = sys.argv[1]
    input_values = [5]  # Valori di input di esempio

    try:
        print(f"Assemblando il file: {assembly_file}...")
        assembler = Assembler(assembly_file)
        initial_memory = assembler.assemble()
        print("Assemblaggio completato.")
        
        print("Avvio simulatore LMC...")
        computer = LMC(initial_memory, input_values)
        computer.run()

        print(f"Contenuto della coda di output: {computer.output_queue}")

    except FileNotFoundError:
        print(f"Errore: Il file '{assembly_file}' non è stato trovato.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

if __name__ == "__main__":
    main()
