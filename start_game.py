from board_logic import game_logic
from drawer import draw

class Start_game:
    def __init__(self):
        self.board = [[""] * 9 for _ in range(9)]
        self.game_logic = game_logic()
        self.difficulty = 0
        self.cells_to_fill = 0
        self.num_moves = 0
        self.row_values = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    def select_difficulty(self):
        print("Selecciona la dificultat:\n1: Fàcil\n2: Mitja\n3: Difícil")
        input_difficult = input("Introdueix la dificultat: ")
        while input_difficult not in ["1", "2", "3"]:
            print("Dificultat no vàlida. Introdueix 1, 2 o 3.")
            input_difficult = input("Introdueix la dificultat: ")
        self.game_logic.set_difficulty(int(input_difficult))
        self.board, self.original_board, solution_board = self.game_logic.fill_board()
        draw(self.board,self.original_board)
        won = False
        while not won:
            self.add_value()
            draw(self.board,self.original_board)
        draw(solution_board, self.original_board)
        input("prem una tecla per a sortir")

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
        if(self.original_board[row_index][col_index]==""):
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
            self.board[row_index][col_index] = cel_value