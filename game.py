from board import Board


class Game:
    def __init__(self, board):
        self.board = board
        self.current_player = 'X'

    def change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def request_move(self):
        while True:
            try:
                x, y = map(int, input(f"Ход {self.current_player}. Введите строку и столбец от 1 до 3 через пробел: ").split())
            except ValueError:
                print("Введите ровно два целых числа через пробел.")
                continue

            if self.board.make_move(x - 1, y - 1, self.current_player):
                return

            print('Недопустимый ход: проверьте координаты, клетку и символ.')


    def play(self):
        while True:
            self.board.display()
            self.request_move()
            if self.board.check():
                self.board.display()
                print(f"Победил игрок {self.current_player}!")
                break
            self.change_player()