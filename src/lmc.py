# Inizio del file: Nome, Cognome, Matricola

class LMCExecutionError(Exception):
    """Eccezione personalizzata per errori durante l'esecuzione dell'LMC."""
    pass


class LMC:

    """Simula il funzionamento del Little Man Computer."""
    def __init__(self, memory, input_values):
        self.memory = memory
        self.input_queue = input_values
        self.output_queue = []
        
        self.accumulator = 0
        self.program_counter = 0
        self.negative_flag = False
    def run(self):
        while True:
            # Controlla se il Program Counter è valido prima di leggere
            if not (0 <= self.program_counter < 100):
                raise LMCExecutionErr(f"Errore: Program Counter fuori dai limiti ({self.program_counter})")

            instruction = self.memory[self.program_counter]
            self.program_counter += 1

            opcode = instruction // 100
            address = instruction % 100

            # --- Inizio Logica Istruzioni ---

            if opcode == 0:  # HLT
                print("Esecuzione terminata (HLT).")
                break

            elif opcode == 1:  # ADD
                value_to_add = self.memory[address]
                result = self.accumulator + value_to_add
                
                # Gestione Flag: si attiva se il risultato supera 999
                self.negative_flag = (result > 999)
                self.accumulator = result % 1000 # Il risultato è sempre modulo 1000

            elif opcode == 2:  # SUB
                value_to_subtract = self.memory[address]
                result = self.accumulator - value_to_subtract

                # Gestione Flag: si attiva se il risultato è negativo
                self.negative_flag = (result < 0)
                self.accumulator = result % 1000 # Il modulo gestisce anche i negativi in modo corretto in Python

            elif opcode == 3:  # STA (Store)
                self.memory[address] = self.accumulator

            elif opcode == 5:  # LDA (Load)
                self.accumulator = self.memory[address]
                self.negative_flag = False # LDA non è un'operazione aritmetica, resetta il flag

            elif opcode == 6:  # BRA (Branch Always)
                self.program_counter = address

            elif opcode == 7:  # BRZ (Branch if Zero)
                if self.accumulator == 0 and not self.negative_flag:
                    self.program_counter = address

            elif opcode == 8:  # BRP (Branch if Positive or Zero)
                if not self.negative_flag:
                    self.program_counter = address

            elif opcode == 9:
                if address == 1:  # INP
                    if not self.input_queue:
                        raise ValueError("Errore fatale: Coda di input vuota!")
                    self.accumulator = self.input_queue.pop(0)
                    self.negative_flag = False # INP resetta il flag
                elif address == 2:  # OUT
                    self.output_queue.append(self.accumulator)
                else:
                    raise ValueError(f"Istruzione non valida: {instruction}")
            else:
                # Se l'opcode non è tra quelli validi (es. 4xx)
                raise ValueError(f"Istruzione non valida: {instruction}")

            # --- Fine Logica Istruzioni ---
