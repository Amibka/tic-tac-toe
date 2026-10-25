def request_move(board, symbol):
    while True:
        try:
            x, y = map(int, input("Введите строку и столбец от 0 до 2: ").split())


        except ValueError:
            print("Введите ровно два целых числа через пробел.")
            continue

        if board.make_move(x, y, symbol):
            return

        print('Недопустимый ход: проверьте координаты, клетку и символ.')