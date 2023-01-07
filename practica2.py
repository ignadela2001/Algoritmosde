tablero_N = input("Introduce el numero de casillas que quieres de alto y ancho: ")

def reina(tablero, r, c):
	for i in range(r):
		if tablero[i][c] == 'Q':
			return False
	(i, j) = (r, c)
	while i >= 0 and j >= 0:
		if tablero[i][j] == 'Q':
			return False
		i = i - 1
		j = j - 1
	(i, j) = (r, c)
	while i >= 0 and j < len(tablero):
		if tablero[i][j] == 'Q':
			return False
		i = i - 1
		j = j + 1

	return True


def solucion(tablero):
	for r in tablero:
		print(str(r).replace(',', '').replace('\'', ''))
	print()


def nReina(tablero, r):
	if r == len(tablero):
		solucion(tablero)
		return
	for i in range(len(tablero)):
		if reina(tablero, r, i):
			tablero[r][i] = 'Q'
			nReina(tablero, r + 1)
			tablero[r][i] = ' '


if _name_ == '_main_':

	N = tablero_N

	tablero = [[' ' for x in range(N)] for y in range(N)]

	nReina(tablero, 0)