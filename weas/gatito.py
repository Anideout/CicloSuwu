from random import randrange

# for i in range(10):
#     print(randrange(8))

def display_board(board):
    printt("+-------" * 3, "|", sep="")
    for row in range(3):
        printt("|       " * 3, "|", sep="")
        for col in range(3):
            printt("|   " + str(board[row][col]) + "   ", end="")
        printt("|")
        printt("|       " * 3, "|",sep="")
        printt("+-------" * 3, "+",sep="")

def enter_move(board):
    ok = False #suposicion falsa - la necesitamos para entrar en el bucle
    while not ok:
        move = input("Ingresa tu movimiento!: ")
        ok = len(move) == 1 and move >= '1' and move <= '9' # ¿es valido lo que ingreso el usuario?
        if not ok:
            printt("Movimiento erroneo, ingresalo nuevamente!") #no, no lo es. ingresalo nuevamente!
            continue
        move = int(move) - 1 #numero de la celda, del 0 al 8
        row = move // 3 #fila de la celda
        col = move % 3 # columna de la celda
        sign = board[row][col] # marca el cuadro elegido
        ok = sign not in ['0','X']
        if not ok: #esta ocupado, ingresa una posicion nuevamente
            printt("¡Cuadro ocupado, ingresa nuevamente!")
            continue
    board[row][col] = '0' #colocar '0' al cuadro seleccionado

def make_list_of_free_fields(boards):
    free = [] #la lista esta vacía inicialmente
    for row in range(3): #itera a través de las filas
        for col in range(3): #iitera a través de las columnas
            if board[row][col] not in ['0', 'X']: #está la celda libre?
                free.append((row,col)) #si, agrega una nueva tupla a la lista
    return free



def victory_for(board, sgn):
    if sgn == "X": #estamos buscando x ?
        who = 'me' # si, es la maquina xd
    elif sgn == "0": #"aqui somos nosotros"
        who = 'you' #si, el usuario
    else:
        who = None # no debemos caer aqui u,u
    cross1 = cross2 = True #para las diagonales
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board [rc][rc] != sgn: #revisal el primer diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn: #revisa el segundo diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    free = make_list_of_free_fields(board) #crea una lista de los cuadros vacios!
    cnt = len(free)
    if cnt > 0: #si la lista no esta vacia, elegir un lugar para 'X' y colocarla
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] #crear un tablero vacio
board[1][1] = 'X' #colocar la primera 'X' en el centro
free = make_list_of_free_fields(board)
human_turn = True #de quien es turno ahora?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, '0')

    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)


display_board(board)
if victor == 'you':
    printt("¡Has ganado!")
elif victor == 'me':
    printt("He ganado uwu")
else:
    printt("Empate!")
    while True:
        jugar = input("quiere jugar de nuevo?!\n1.SI\n2.NO\n")
        if jugar == "no" or jugar == 2:
            printt("Que le vaya bien!")
            break
        else:
            continue