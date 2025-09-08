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

        # Un set di tutte le possibili istruzioni LMC per riconoscerle.
        # È in maiuscolo perché normalizzeremo tutto in maiuscolo per essere case-insensitive.
        INSTRUCTIONS = {"ADD", "SUB", "STA", "LDA", "BRA", "BRZ", "BRP", "INP", "OUT", "HLT", "DAT"}

        address = 0
        for line in lines:
            # 1. Pulizia della riga: togli commenti e spazi inutili
            line_no_comment = line.split('//')[0]
            clean_line = line_no_comment.strip().upper() # .upper() per renderlo case-insensitive

            # 2. Se la riga è vuota dopo la pulizia, la saltiamo
            if not clean_line:
                continue

            # 3. Dividiamo la riga in "parole"
            parts = clean_line.split()
            
            # 4. Controlliamo se la prima parola è un'etichetta
            # La logica è: se la prima parola NON è un'istruzione conosciuta, DEVE essere un'etichetta.
            if parts[0] not in INSTRUCTIONS:
                label = parts[0]
                
                # Controlliamo se l'etichetta è già stata definita. Non si può.
                if label in self.labels:
                    raise ValueError(f"Errore: Etichetta '{label}' definita più di una volta.")
                
                # Memorizziamo l'etichetta e il suo indirizzo corrente nel nostro dizionario
                print(f"Trovata etichetta '{label}' all'indirizzo {address}") # Utile per il debug
                self.labels[label] = address
            
            # 5. Incrementiamo l'indirizzo per la prossima riga che contiene codice
            # Ogni riga non vuota e non di solo commento occupa una cella di memoria.
            address += 1


    def _second_pass(self, lines):

        # Mappa delle istruzioni assembly ai loro opcode numerici.
        OPCODES = {
            "ADD": 100, "SUB": 200, "STA": 300, "LDA": 500,
            "BRA": 600, "BRZ": 700, "BRP": 800
        }

        # Le istruzioni senza argomento hanno un codice macchina fisso.
        SPECIAL_OPCODES = {"INP": 901, "OUT": 902, "HLT": 000}

        address = 0
        for line in lines:
            # 1. Pulizia della riga (esattamente come nella prima passata)
            line_no_comment = line.split('//')[0]
            clean_line = line_no_comment.strip().upper()

            if not clean_line:
                continue

            parts = clean_line.split()

            # 2. Rimuoviamo l'etichetta se presente, ci serve solo istruzione e argomento
            # Se la prima parola non è un'istruzione conosciuta, è un'etichetta. La saltiamo.
            if parts[0] in OPCODES or parts[0] in SPECIAL_OPCODES or parts[0] == "DAT":
                instruction_parts = parts
            else:
                instruction_parts = parts[1:] # Prendi tutto tranne la prima parola (l'etichetta)

            instruction = instruction_parts[0]
            machine_code = 0 # Valore di default

            # 3. Traduciamo l'istruzione in codice macchina
            if instruction in OPCODES:
                arg = instruction_parts[1]
                # L'argomento è un'etichetta o un numero?
                if arg in self.labels:
                    # È un'etichetta, prendiamo il suo indirizzo dalla mappa
                    machine_code = OPCODES[instruction] + self.labels[arg]
                else:
                    # È un numero, lo convertiamo e lo sommiamo
                    machine_code = OPCODES[instruction] + int(arg)

            elif instruction in SPECIAL_OPCODES:
                machine_code = SPECIAL_OPCODES[instruction]

            elif instruction == "DAT":
                # L'istruzione DAT memorizza un valore direttamente.
                # Se non c'è un valore (solo "DAT"), per convenzione è 0.
                if len(instruction_parts) > 1:
                    machine_code = int(instruction_parts[1])
                else:
                    machine_code = 0

            # 4. Scriviamo il codice macchina calcolato nella memoria all'indirizzo corrente
            self.memory[address] = machine_code

            # 5. Passiamo all'indirizzo successivo
            address += 1
