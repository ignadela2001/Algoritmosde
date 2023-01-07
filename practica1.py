Teclado = [[1,2,3],[4,5,6], [7,8,9], [None, 0, None]]

def Contar_elementos_matriz(matriz):
 contador_movimientos = 0
 for row in range(len(matriz)):
  for col in range (len(matriz[row])):
      if matriz[row][col] != None:
          contador_movimientos = contador_movimientos + 1
 return contador_movimientos

def Movimientos_posibles(tablero, movimientos, punto_inicio):
    if movimientos == 0:
        return 0
    for row in range(len(tablero)):
        for col in range (len(tablero[row])):
            if(tablero[row][col] == punto_inicio):
                if(row==0 and col == 0):
                   return 2+Movimientos_posibles(tablero,movimientos-1,tablero[row+1][col+2])+Movimientos_posibles(tablero,movimientos-1,tablero[row+2][col+1])
                elif(row==1 and col == 0):
                    return 3+Movimientos_posibles(tablero,movimientos-1,tablero[row+1][col+2])+Movimientos_posibles(tablero,movimientos-1,tablero[row-1][col+2])+Movimientos_posibles(tablero,movimientos-1,tablero[row+2][col+1])
                elif(row==2 and col == 0):
                    return 2+Movimientos_posibles(tablero,movimientos-1,tablero[row-1][col+2])+Movimientos_posibles(tablero,movimientos-1,tablero[row-2][col+1])
                elif(row== 3 and col == 1):
                    return 2+Movimientos_posibles(tablero,movimientos-1,tablero[row-2][col+1])+Movimientos_posibles(tablero,movimientos-1,tablero[row-2][col-1])
                elif(row==0 and col == 1):
                   return 2+Movimientos_posibles(tablero,movimientos-1,tablero[row+2][col+1])+Movimientos_posibles(tablero,movimientos-1,tablero[row+2][col-1])
                elif(row==1 and col == 1):
                    return 0
                elif(row==2 and col == 1):
                    return 2+Movimientos_posibles(tablero,movimientos-1,tablero[row-2][col+1])+Movimientos_posibles(tablero,movimientos-1,tablero[row-2][col-1])
                elif(row==0 and col == 2):
                   return 2+Movimientos_posibles(tablero,movimientos-1,tablero[row+2][col-1])+Movimientos_posibles(tablero,movimientos-1,tablero[row+1][col-2])
                elif(row==1 and col == 2):
                    return 3+Movimientos_posibles(tablero,movimientos-1,tablero[row+2][col-1])+Movimientos_posibles(tablero,movimientos-1,tablero[row-1][col-2])+Movimientos_posibles(tablero,movimientos-1,tablero[row+1][col-2])
                elif(row==2 and col == 2):
                    return 2+Movimientos_posibles(tablero,movimientos-1,tablero[row-2][col-1])+Movimientos_posibles(tablero,movimientos-1,tablero[row-1][col-2])
                                

def Movimientos_validos_caballo2(tablero, movimientos):
 contador_movimientos = 0
 for posicion_inicial in range(Contar_elementos_matriz(tablero)):
   contador_movimientos = contador_movimientos + Movimientos_posibles(tablero, movimientos, posicion_inicial)
 return contador_movimientos

print(Movimientos_validos_caballo2(Teclado, 1))