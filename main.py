from board import Board
from game import request_move


def main():
    board = Board()
    board.display()

    request_move(board, 'X')

    board.display()


if __name__ == '__main__':
    main()