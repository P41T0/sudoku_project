from game_logic import game_logic
from drawer import draw

class Start_game:
    def __init__(self):
        self.board = [[""] * 9 for _ in range(9)]
        self.game_logic = game_logic()
        self.difficulty = 0
        self.cells_to_fill = 0
        self.num_moves = 0

    def select_difficulty(self):
        print("Selecciona la dificultat:\n1: Fàcil\n2: Mitja\n3: Difícil")
        input_difficult = input("Introdueix la dificultat: ")
        while input_difficult not in ["1", "2", "3"]:
            print("Dificultat no vàlida. Introdueix 1, 2 o 3.")
            input_difficult = input("Introdueix la dificultat: ")
        self.game_logic.set_difficulty(int(input_difficult))
        self.board = self.game_logic.fill_board()
        draw(self.board)