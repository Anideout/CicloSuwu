import chess
import os, time


#create board
board = chess.Board()
print(board)

    
#variables
contMoves = 0
bool = False 

Empezar = input("Empezar SI.   NO.")

if Empezar.lower() == "s":
    bool = True
    file = open("Registro_De_Partida.txt", "w")
else:
    print("xaoooxaooax")
    time.sleep(1)
        
while bool:
    try:
        legalMoves = board.legal_moves
        
        #escribir jugada uwu:
        jugada = input("Jugada: \n")
        
        contMoves += 1
        
        if contMoves == 2:
            file.write(os.linesep)
            contMoves = 0
            
        if jugada == "Legalmoves":
            print("\n Estas son las jugadas legadles que puedes realizar en este momento: \n {}", legalMoves)
            
        elif jugada == "back":
            board.pop(chess.Move.null())
            
            
        elif jugada == "exit":
            time.sleep(1)
            file.close()
            bool = False
            
        else:
            try:
                move = chess.Move.from_uci(jugada)
                if move in legalMoves:
                    #imprime pieza movida y cuadro de destino 
                    print(board.piece_at(move.from_square), move.from_square, "->", move.to_square)
                    board.push(move)
                    highlight_square(board, move.from_square)
                    highlight_square(board, move.to_square)
                    print(board)
                else:
                    print("Invalid move")
            except:
                print("Movimiento Invalido! ")

        if board.is_checkmate():
            print("-------------\nJaque Mate! \n-------------")
            time.sleep(1)
            pregunta = input("Quieres jugar de nuevo ?     SI   ,  NO\n")
            if pregunta == "YES" or pregunta == "yes":
                board = chess.Board()
                print(board)

        elif pregunta == "NO" or pregunta == "no":
            print("xao nos vemos uwuuu ")
            time.sleep(0, 30)
            file.close()
            bool = False

        else:
            print("opcion invalida u.u ")
    except:
        print("\nMovimiento invalido! \n")
        print("n{}". format(board))

def highlight_square(board, square):
    rank = square // 8
    file = square % 8
    rank_name = "ABCDEFGH"[rank]
    file_name = "12345678"[file]
    print("\033[1;31m" + rank_name + file_name + "\033[0m", end=" ")    