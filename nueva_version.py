#Diego Chacon Pimentel 203414
#Andy Omar Franco Bermudez 203717
import tkinter as tk


grammar_variable= {
    'terminals': {'A', '1', '2', '3', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'},
    'non_terminals': {'DV', 'X', 'N', 'Y', 'L', 'PYC', 'TV'},
    'start': 'DV',
    'DV': [('TV', 'X')],
    'X': [('N', 'Y')],
    'Y': [('L', 'PYC')],
    'PYC': [';'],
    'TV': [('A',)],
    'N': [('1',), ('2',), ('3',)],
    'L': [('a',), ('b',), ('c',), ('d',), ('e',), ('f',), ('g',), ('h',), ('i',), ('j',), ('k',), ('l',), ('m',), ('n',), ('o',), ('p',), ('q',), ('r',), ('s',), ('t',), ('u',), ('v',), ('w',), ('x',), ('y',), ('z',)],
}


grammar_condicional = {
    'terminals': {'(', ')', ':', ';', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '>', '<', '=', 'C'},
    'non_terminals': {'DC', 'A', 'B', 'N', 'Y', 'PA', 'Y2', 'V', 'Y3', 'OC', 'Y5', 'Y6', 'PC', 'Y7', 'D', 'Y8', 'PYC', 'DP', 'Y4'},
    'start': 'DC',
    'DC': [('A', 'Y')],
    'A': [('B', 'N')],
    'B': [('C',)],
    'N': [('1',)],
    'Y': [('PA', 'Y2')],
    'PA': [('(',)],
    'Y2': [('V', 'Y3'), ('V', 'Y4')],
    'V': [('a',), ('b',), ('c',), ('d',), ('e',), ('f',), ('g',), ('h',), ('i',), ('j',), ('k',), ('l',), ('m',), ('n',), ('o',), ('p',), ('q',), ('r',), ('s',), ('t',), ('u',), ('v',), ('w',), ('x',), ('y',), ('z',)],
    'Y3': [('OC', 'Y5')],
    'OC': ['>', '<', '='],
    'Y5': [('V', 'Y6')],
    'Y6': [('PC', 'Y7')],
    'PC': [(')',)],
    'Y7': [('DP', 'PYC')],
    'DP': [(':')],
    'PYC': [(';',)],
    'Y4': [('OC', 'Y8')],
    'Y8': [('D', 'Y6')],
    'D': [('1',), ('2',), ('3',), ('4',), ('5',), ('6',), ('7',), ('8',), ('9',)],
}

grammar_funcion ={
    'terminals': {'(', ')', ':', ';', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'},
    'non_terminals': {'DF', 'Z1', 'W1', 'Z2', 'Z3', 'Z4','W2', 'W3','W4','A1', 'A2', 'A3', 'A4', 'A5','PA', 'PC', 'DP', 'PYC', 'V'},
    'start': 'DF',
    'DF': [('Z1', 'W1')],
    'Z1': [('A1', 'A2')],
    'A1': [('i',)],
    'A2': [('A3', 'A4')],
    'A3': [('n',)],
    'A4': [('A1', 'A5')],
    'A5': [('t',)],
    'W1': [('V', 'Z2')],
    'Z2': [('PA', 'W2')],
    'PA': [('(',)],
    'W2': [('V', 'Z3')],
    'V': [('a',), ('b',), ('c',), ('d',), ('e',), ('f',), ('g',), ('h',), ('i',), ('j',), ('k',), ('l',), ('m',), ('n',), ('o',), ('p',), ('q',), ('r',), ('s',), ('t',), ('u',), ('v',), ('w',), ('x',), ('y',), ('z',)],
    'Z3': [('PC', 'W3')],
    'PC': [(')',)],
    'W3': [('DP', 'PYC')],
    'DP': [(':')],
    'PYC': [(';',)],
    
}
grammar_ciclo = {
    'terminals': {'(', ')', ':', ';', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '>', '<', '=', 'F', '+', '-'},
    'non_terminals': {'DCA', 'Q1', 'A', 'B', 'R1', 'PA','CU', 'V','S1','IG', 'S2', 'R2', 'CO', 'Q3','A2', 'A3', 'OC', 'R3', 'Q4', 'CT', 'SR','M', 'R4', 'PC', 'Q5', 'DP', 'PYC', 'D'},
    'start': 'DCA',
    'DCA': [('Q1', 'R1')],
    'Q1': [('A', 'B')],
    'A': [('F')],
    'B': [('1')],
    'R1': [('PA', 'CU')],
    'PA': [('(')],
    'CU': [('V', 'S1')],
    'V': [('a',), ('b',), ('c',), ('d',), ('e',), ('f',), ('g',), ('h',), ('i',), ('j',), ('k',), ('l',), ('m',), ('n',), ('o',), ('p',), ('q',), ('r',), ('s',), ('t',), ('u',), ('v',), ('w',), ('x',), ('y',), ('z',)],
    'S1': [('IG', 'S2')],
    'IG': [('=')],
    'S2': [('D', 'R2')],
    'R2': [('CO', 'Q3')],
    'CO': [(',')],
    'Q3': [('A2', 'R3')],
    'A2': [('V', 'A3')],
    'A3': [('OC', 'V')],
    'OC': [('>', '<',)],
    'R3': [('CO', 'Q4')],
    'Q4': [('CT', 'R4')],
    'CT': [('V', 'SR')],
    'SR': [('M', 'M')],
    'M': [('+',), ('-',)],
    'R4': [('PC', 'Q5')],
    'PC': [(')')],
    'Q5': [('DP', 'PYC')],
    'DP': [(':')],
    'PYC': [(';')],
    'D': [('1',), ('2',), ('3',), ('4',), ('5',), ('6',), ('7',), ('8',), ('9',)],
}


class PDA:
    def __init__(self, grammars):
        self.stack = ['$']
        self.input_string = ""
        self.grammars = grammars
        self.current_grammar = None

    def set_grammar(self, grammar_name):
        if grammar_name in self.grammars:
            self.current_grammar = self.grammars[grammar_name]
            self.stack = ['$']
            self.stack.append(self.current_grammar['start'])
        else:
            
            print(f"Error: La gramatica no se encontro.")

    def detect_grammar(self, input_string):
        if 'init' in input_string:
            return 'funcion'
        elif 'C1' in input_string:
            return 'condicional'
        elif 'F1' in input_string:
            return 'ciclo'
        elif 'A1' in input_string:
            return 'variable'
        else:
            return 'Error'

    def process_input(self, input_string, result_grammar_label, result_stack_label):
        self.input_string = input_string
        grammar_to_use = self.detect_grammar(input_string)
        self.set_grammar(grammar_to_use)

        while self.stack and self.current_grammar:
            x = self.stack[-1]
            a = self.input_string[0] if self.input_string else None
            current_text = result_stack_label.cget("text")
            separator = '' if not current_text else '\n'
            result_stack_label.config(text=f"{current_text} {separator} {' - '.join(self.stack)}")
            

            if x in self.current_grammar.get('terminals', []):
                if x == a or (x.isalpha() and a.isalpha()):
                    self.stack.pop()
                    if a:
                        self.input_string = self.input_string[1:]
                else:
                    print("Error: No coincide con el terminal esperado.")
                    break
            elif x in self.current_grammar['non_terminals']:
                if x == 'IG':
                    if a == '=':
                        self.stack.pop()
                        if a:
                            self.input_string = self.input_string[1:]
                    else:
                        print("Error: No coincide con el terminal esperado.")
                        break
                elif x in self.current_grammar:
                    self.stack.pop()
                    production = self.current_grammar[x][0]
                    for symbol in production[::-1]:
                        if symbol != 'epsilon':
                            self.stack.append(symbol)
                else:
                    print("Error: No hay producción para el no terminal.")
                    break
            elif x == '$' and not self.input_string:
                print("Cadena aceptada.")
                break
            elif x == ';' and a == ';':
                self.stack.pop()
                if a:
                    self.input_string = self.input_string[1:]
            else:
                result_stack_label.config(text=f"Pila: No valida")
                break

class PDAGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("600x600")
        self.configure(bg="#333")
        self._frame = None
        self.crear_interfaz()

    def crear_interfaz(self):
        self.label = tk.Label(self, text="PikaPy", font=('Arial', 16),bg="#333",fg="yellow")
        self.label.pack(pady=10)
        self.input_label = tk.Label(self, text="Ingrese una cadena:", font=('Arial', 16),bg="#333",fg="white")
        self.input_label.pack(pady=10)
        
        self.input_entry = tk.Entry(self, font=('Arial', 16), width=20, relief="solid", borderwidth=2)
        self.input_entry.pack(pady=10)
        
        estilo_boton = {
            'font': ('Arial', 20, 'bold'), 
            'fg': '#333',
            'bg': 'white',
            'width': 11,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }
        
        self.verify_button = tk.Button(self, text="Verificar", command=self.verify_input, **estilo_boton)
        self.verify_button.pack(pady=10)
        
        self.result_grammar_label = tk.Label(self, text="Gramática utilizada:",font=('Arial', 12),bg="#333",fg="white")
        self.result_grammar_label.pack(pady=10)
        
        self.result_stack_label = tk.Label(self, text="Pila:", font=('Arial', 12),bg="#333",fg="white")
        self.result_stack_label.pack(pady=10)

        self.pda = PDA({'variable': grammar_variable, 'condicional': grammar_condicional, 'funcion': grammar_funcion, 'ciclo': grammar_ciclo})

    def verify_input(self):
        input_string = self.input_entry.get()
        self.result_stack_label.config(text="Pila:") 
        self.pda.process_input(input_string,self.result_grammar_label, self.result_stack_label)
        self.result_grammar_label.config(text=f"Gramática utilizada: {self.pda.detect_grammar(input_string)}")
       

if __name__ == "__main__":
    app = PDAGUI()
    app.mainloop()

