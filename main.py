from board import Board
from game import Game


def main():
    while True:
        board = Board()
        game = Game(board)
        game.play()

        if input("Хотите сыграть еще раз? (y/n): ").lower() != 'y':
            break


if __name__ == '__main__':
    main()