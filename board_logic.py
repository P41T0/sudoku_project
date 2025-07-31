import random
from drawer import draw


class game_logic:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.original_board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution_board = [[0 for _ in range(9)] for _ in range(9)]
        self.cells_to_erase = 0
        self.won = False

    def is_valid(self, fila, columna, valor):
        if valor in self.board[fila]:
            return False
        if any(self.board[i][columna] == valor for i in range(9)):
            return False
        start_row = (fila // 3) * 3
        start_col = (columna // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == valor:
                    return False
        return True

    def solve_board(self):
        for fila in range(9):
            for columna in range(9):
                if self.board[fila][columna] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for valor in nums:
                        if self.is_valid(fila, columna, valor):
                            self.board[fila][columna] = valor
                            self.solution_board[fila][columna] = valor
                            if self.solve_board():
                                return True
                            self.board[fila][columna] = 0  # backtrack
                    return False
        return True

    def erase_cells(self):
        while self.cells_to_erase > 0:
            fila = random.randint(0, 8)
            columna = random.randint(0, 8)
            if self.board[fila][columna] != "":
                self.board[fila][columna] = ""
                self.cells_to_erase -= 1

    def set_original_board(self):
        for r in range(9):
            for c in range(9):
                self.original_board[r][c] = self.board[r][c]

    def set_difficulty(self, difficulty):
        if difficulty == 1:
            self.cells_to_erase = 36
        elif difficulty == 2:
            self.cells_to_erase = 45
        elif difficulty == 3:
            self.cells_to_erase = 54

    def fill_board(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solve_board()
        self.erase_cells()
        self.set_original_board()
        draw(self.board, self.original_board)

    def draw_board(self):
        draw(self.board, self.original_board)

    def check_position(self, row_index, col_index):
        return self.original_board[row_index][col_index] == ""

    def add_value(self, row_index, col_index, cel_value):
        self.board[row_index][col_index] = cel_value
        draw(self.board, self.original_board)
        print("entro aqui")

    def get_won(self):
        self.check_win()
        return self.won

    def check_win(self):
        print("entro")
        for r in range(0, 9):
            for c in range(0, 9):
                if self.board[r][c] != self.solution_board[r][c]:
                    return
        self.won = True

    def get_hint(self):
        if self.won == False:
            while True:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                if self.original_board[row][col] == "":
                    if self.board[row][col] != self.solution_board[row][col]:
                        self.board[row][col] = self.solution_board[row][col]
                        break
            draw(self.board, self.original_board)
