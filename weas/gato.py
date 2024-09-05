from random import randrange


def display_tab(tablero):
    printt("+-------" * 3, "|", sep="")
    for row in range(3):
        printt("|       " * 3, "|", sep="")
        for col in range(3):
            printt("|   " + str(tablero[row][col]) + "   ", end="")
        printt("|")
        printt("|       " * 3, "|", sep="")
        printt("+-------" * 3, "+", sep="")

def ingrese_movimiento(tablero):
    ok = False
    while not ok:
        movimiento = input("Ingresa tu movimiento: \n")
        ok = len(movimiento) == 1 and movimiento >= '1' and movimiento <= '9'
        if not ok:
            printt("Movimiento erroneo, ingresalo nuevamente!!\n")
            continue
        movimiento = int(movimiento) - 1
        row = movimiento // 3
        col = movimiento % 3
        sign = tablero[row][col]
        ok = sign not in ['0', 'X']
        if not ok:
            printt("Cuadro ocupado!, ingresalo nuevamente..\n")
            continue
    tablero[row][col] = '0'

def campos_libre(tablero):
    libre = []
    for row in range(3):
        for col in range(3):
            if tablero[row][col] not in ['0', 'X']:
                libre.append((row,col))
    return libre

def victoria(tablero, sgn):
    if sgn == "X":
        quien = 'Yo'
    elif sgn == "0":
        quien = 'Tu'
    else:
        quien = None
    equis1 = equis2 = True
    for rc in range(3):
        if tablero[rc][0] == sgn and tablero[rc][1] == sgn and tablero[rc][2] == sgn:
            return quien
        if tablero[0][rc] == sgn and tablero[1][rc] == sgn and tablero[2][rc] == sgn:
            return quien
        if tablero[rc][rc] != sgn:
            equis1 = False
        if tablero[2 - rc][2- rc] != sgn:
            equis2 = False
    if equis1 or equis2:
        return quien
    return None

def mover(tablero):
    libre = campos_libre(tablero)
    cnt = len(libre)
    if cnt > 0:
        this = randrange(cnt)
        row, col = libre[this]
        tablero[row][col] = 'X'


tablero = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
tablero[1][1] = 'X'
libre = campos_libre(tablero)
turno = True
while len(libre):
    display_tab(tablero)
    if turno:
        ingrese_movimiento(tablero)
        victor = victoria(tablero, '0')

    else:
        mover(tablero)
        victor = victoria(tablero, 'X')
    if victor != None:
        break
    turno = not turno
    libre = campos_libre(tablero)


display_tab(tablero)
if victor == 'tu':
    printt("Has ganado!!!\n")
elif victor == 'yo':
    printt("he ganado!\n")
else:
    printt("Empate!\n")