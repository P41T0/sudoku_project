from board_logic import game_logic

class Start_game:
    def __init__(self):
        self.game_logic = game_logic()
        self.difficulty = 0
        self.cells_to_fill = 0
        self.num_moves = 0
        self.row_values = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        self.won = False

    def select_difficulty(self):
        print("Selecciona la dificultat:\n1: Fàcil\n2: Mitja\n3: Difícil")
        input_difficult = input("Introdueix la dificultat: ")
        while input_difficult not in ["1", "2", "3"]:
            print("Dificultat no vàlida. Introdueix 1, 2 o 3.")
            input_difficult = input("Introdueix la dificultat: ")
        self.game_logic.set_difficulty(int(input_difficult))
        self.game_logic.fill_board()
        won = False
        while not won:
            self.select_action()
        input("prem una tecla per a sortir")

    def select_action(self):
        print("Selecciona una acció:\n1: Afegir número\n2: Eliminar número")
        while True:
            action = input("Introdueix l'acció: ")
            if action in ["1", "2"]:
                break
        if action == "1":
            self.add_value()
        elif action == "2":
            self.delete_value()

    def delete_value(self):
        while True:
            row = input("Introdueix el valor de la fila (A-I): ")
            if (len(row) == 1 and row.upper() in self.row_values):
                row_index = self.row_values.index(row.upper())
                break
        while True:
            col_index = input("Introdueix el valor de la columna (1-9): ")
            try:
                col_index = int(col_index)
                if 1 <= col_index <= 9:
                    col_index = col_index - 1
                    break
                else:
                    print("valor incorrecte")
            except:
                print("valor incorrecte")
        if(self.game_logic.check_position(row_index, col_index)):
            self.game_logic.add_value("")

    def add_value(self):
        while True:
            row = input("Introdueix el valor de la fila (A-I): ")
            if (len(row) == 1 and row.upper() in self.row_values):
                row_index = self.row_values.index(row.upper())
                break
        while True:
            col_index = input("Introdueix el valor de la columna (1-9): ")
            try:
                col_index = int(col_index)
                if 1 <= col_index <= 9:
                    col_index = col_index - 1
                    break
                else:
                    print("valor incorrecte")
            except:
                print("valor incorrecte")
        if(self.game_logic.check_position(row_index, col_index)):
            while True:
                cel_value = input("Introdueix el valor de la cel·la (1-9): ")
                try:
                    cel_value = int(cel_value)
                    if 1 <= cel_value <= 9:
                        break
                    else:
                        print("valor incorrecte")
                except:
                    print("valor incorrecte")
            self.game_logic.add_value(row_index, col_index, cel_value)
        else: 
            print("Has intentat modificar un valor ja existent")