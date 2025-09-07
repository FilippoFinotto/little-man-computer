# Inizio del file: Nome, Cognome, Matricola

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
        """Esegue il programma fino all'istruzione HLT o a un errore."""
        while True:
            instruction = self.memory[self.program_counter]
            self.program_counter += 1

            opcode = instruction // 100
            address = instruction % 100

            if opcode == 0: # HLT
                print("Esecuzione terminata (HLT).")
                break
            elif opcode == 1: # ADD
                # DA IMPLEMENTARE: Logica per ADD
                pass
            elif opcode == 2: # SUB
                # DA IMPLEMENTARE: Logica per SUB
                pass
            elif opcode == 3: # STA
                self.memory[address] = self.accumulator
            # ... implementa qui tutti gli altri opcode (5, 6, 7, 8, 9) ...
            elif opcode == 9 and address == 1: # INP
                if self.input_queue:
                    self.accumulator = self.input_queue.pop(0)
                else:
                    raise ValueError("Coda di input vuota!")
            elif opcode == 9 and address == 2: # OUT
                self.output_queue.append(self.accumulator)
            else:
                raise ValueError(f"Istruzione non valida: {instruction}")

            # DA IMPLEMENTARE: Gestione dell'overflow e del flag
