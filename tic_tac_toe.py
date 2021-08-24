#крестики нолики

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
    while True:
        if any([
            F[0].count('X') == 3,
            F[1].count('X') == 3,
            F[2].count('X') == 3
            ]):
        	return 'win X'
        elif any([
            F[0].count('O') == 3,
            F[1].count('O') == 3,
            F[2].count('O') == 3,
            ]):
            return 'win O'
        break


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
	elif win_O == win_check():
		print('Игра окончена, победил O')
		break
	elif end_game == end_game_check():
		print('Конец игры')
		break
	a = input('Чья очередь ставить -  X или O ?' )
	if a != 'X' and a != 'O':
		print('Неверно введен знак, введите X или O ! (engl upper)')
		continue
	elif a == 'X':
		x = int(input('Введите строку (1 2 3) -')) - 1
		y = int(input('Введите столбец (1 2 3) -')) - 1
		if F[x][y] == 0:
			F[x][y] = 'X'
			win_check() 
		else:
			print('Поле занято')
			continue
	else: # a == O
		x = int(input('Введите строку (1 2 3) -')) - 1
		y = int(input('Введите столбец (1 2 3) -')) - 1
		if F[x][y] == 0:
			F[x][y] = 'O'
			win_check()
		else:
			print('Поле занято')
			continue
	print_field()
