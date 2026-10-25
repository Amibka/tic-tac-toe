class Board:
    def __init__(self):
        ROWS = 3
        COLS = 3
        self._board = [['.' for _ in range(COLS)] for _ in range(ROWS)]

    def display(self):
        for row in self._board:
            print(' '.join(row))

    def make_move(self, x, y, symbol):
        if self.is_valid_move(x, y, symbol):
            self._write_move(x, y, symbol)
            return True
        return False

    def _write_move(self, x, y, symbol):
        self._board[x][y] = symbol

    def is_valid_move(self, x, y, symbol):
        return (
            self.check_coordinates(x, y)
            and self.is_valid_symbol(symbol)
            and self.is_cell_empty(x, y)
        )

    def is_cell_empty(self, x, y):
        return self._board[x][y] == '.'

    @staticmethod
    def is_valid_symbol(symbol):
        return symbol in ('X', 'O')

    @staticmethod
    def check_coordinates(x, y):
        return 0 <= x < 3 and 0 <= y < 3

    @property
    def cells(self):
        return self._board

    def check(self):
        if self.check_winner():
            return "win"
        if self.check_draw():
            return "draw"
        return False

    def check_winner(self):
        for i in range(3):
            if self._board[i][0] == self._board[i][1] == self._board[i][2] != '.':
                return True

            if self._board[0][i] == self._board[1][i] == self._board[2][i] != '.':
                return True

        if self._board[0][0] == self._board[1][1] == self._board[2][2] != '.':
            return True

        if self._board[0][2] == self._board[1][1] == self._board[2][0] != '.':
            return True

        return False

    def check_draw(self):
        for row in self._board:
            if '.' in row:
                return False
        return True