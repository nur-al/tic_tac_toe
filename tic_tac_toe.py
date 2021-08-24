# крестики нолики

def print_field():
    for i in range(3):
        print(F[i])


def end_game_check():
    end_game = 0
    for i in range(3):
        for j in range(3):
            if all([F[i][j]]):
                end_game += 1
    if end_game == 9:
        print('Игра окончена')
        return 'end'


def win_check():
    for i in range(3):
        if F[i].count('X') == 3:
            return 'win X'
        if F[i].count('O') == 3:
            return 'win O'
    if F[0][0] == 'X' and F[1][0] == 'X' and F[2][0] == 'X': return 'win X'
    if F[0][1] == 'X' and F[1][1] == 'X' and F[2][1] == 'X': return 'win X'
    if F[0][2] == 'X' and F[1][2] == 'X' and F[2][2] == 'X': return 'win X'
    if F[0][0] == 'X' and F[1][1] == 'X' and F[2][2] == 'X': return 'win X'
    if F[0][0] == 'O' and F[1][0] == 'O' and F[2][0] == 'O': return 'win O'
    if F[0][1] == 'O' and F[1][1] == 'O' and F[2][1] == 'O': return 'win O'
    if F[0][2] == 'O' and F[1][2] == 'O' and F[2][2] == 'O': return 'win O'
    if F[0][0] == 'O' and F[1][1] == 'O' and F[2][2] == 'O': return 'win O'




F = [0] * 3
for i in range(3):
    F[i] = [0] * 3

print_field()

while True:
    win_X = 'win X'
    win_O = 'win O'
    end_game = 'end'
    if win_X == win_check():
        print('Игра окончена, победил X')
        break
    if win_O == win_check():
        print('Игра окончена, победил O')
        break
    if end_game == end_game_check():
        print('Конец игры')
        break
    a = input('Чья очередь ставить -  X или O ?')
    if a != 'X' and a != 'O':
        print('Неверно введен знак, введите X или O ! (engl upper)')
        continue
    x = int(input('Введите строку (1 2 3) -')) - 1
    y = int(input('Введите столбец (1 2 3) -')) - 1
    if x < 0 or x > 2 or y < 0 or y > 2:
        print('Неверно введены данные, повторите ввод (цифры от 1 до 3 включительно)')
        continue
    if a == 'X':
        if not F[x][y]:
            F[x][y] = 'X'
            win_check()
        else:
            print('Поле занято')
            continue
    if a == 'O':
        if not F[x][y]:
            F[x][y] = 'O'
            win_check()
        else:
            print('Поле занято')
            continue
    print_field()
