import chess
import os
import time as t 
import subprocess as s

#create board
board = chess.Board()
print(board)

def ClearScree():
    s.run("cls",shell=True)
    
#variables
contMoves = 0
bool = False 

Empezar = input("Empezar SI.   NO.")

if Empezar == "s" or Empezar == "S":
    Bool = True
    file = open("Registro_De_Partida.txt", "w")
else:
    print("xaoooxaooax")
    t.sleep(1)
    
while Bool:
    try:
        legalMoves = board.legal_moves
        
        #escribir jugada uwu:
        jugada = input("Jugada: \n")
        
        contMoves += 1
        
        if contMoves == 2:
            file.write(os.linesep)
            contMoves = 0
            
        if jugada == "Legalmoves":
            print("\n Estas son las jugadas legadles que puedes realizar en este momento: \n {}".format(legalMoves))
            
        if jugada == "back":
            board.pop()
            
        if jugada == "exit":
            t.sleep()
            file.close()
            
            bool = False
            
        
        #imprime el tablero actual en pantalla
        print(board)
            
            
        if board.is_checkmate():
            print("-------------\nJQUE MATE \n --------")
            t.sleep(1)
            pregunta = input("Quieres repetir la partida? SI   ,  No\n")
            if pregunta == "s" or pregunta == "S":
                board = chess.Board()
                
        elif pregunta == "n" or pregunta == "N":
            print("xao nos vemos uwuuu ")
            t.sleep(0, 30)
            file.close()
            Bool = False
            
        else:
            print("opcion no valida")
            
            
        #detectar tablas por repetición
        
        if board.is_fivefold_repetition():
            print("--------------------\nTablas por repeticion\n--------------")
            
        #detecetar tablas por no comer ni mover peon en 75 movimientos    
        if board.is_seventyfive_moves():
            print("--------------\nTablas por no comer ni mover ni peon\n ---------------")
        #detectar jaque    
        if board.is_check():
            print("---------------\nJAQUE\n-----------")
            
        #si se escribe se reinicia el juego
        if jugada == "Restar":
            board = chess.Board()
            print(board)

    except:
        print("\njugada invalida\n")
        print("n{}".format(board))            