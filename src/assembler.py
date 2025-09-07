# Inizio del file: Nome, Cognome, Matricola (come richiesto)

class Assembler:
    """
    La classe Assembler traduce un file sorgente assembly per LMC
    in una lista di interi (codice macchina).
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.labels = {}  # Dizionario per etichette -> indirizzo
        self.memory = [0] * 100

    def assemble(self):
        """Metodo principale che orchestra il processo."""
        with open(self.file_path, 'r') as f:
            lines = f.readlines()

        self._first_pass(lines)
        self._second_pass(lines)
        return self.memory

    def _first_pass(self, lines):
        """Prima passata: trova e memorizza tutte le etichette."""
        address = 0
        for line in lines:
            # DA IMPLEMENTARE: Analizza la riga. Se c'è un'etichetta,
            # la salvi in self.labels con l'indirizzo corrente.
            # L'indirizzo aumenta solo se c'è un'istruzione.
            # Esempio: "LOOP INP" -> self.labels["LOOP"] = address
            pass

    def _second_pass(self, lines):
        """Seconda passata: traduce le istruzioni in codice macchina."""
        address = 0
        for line in lines:
            # DA IMPLEMENTARE: Traduci ogni istruzione in un numero
            # e salvalo in self.memory[address].
            # Esempio: "ADD 15" -> 115
            # Esempio: "BRA LOOP" -> 600 + self.labels["LOOP"]
            pass
