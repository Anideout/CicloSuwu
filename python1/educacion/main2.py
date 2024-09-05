from funciones2 import * 

user_admin = "admin"
passw  = "1234"
banMenu = True
while banMenu:
    print("\t\tCall of honor!\n")
    print("\tSistema de gestion de jugadores! --EPICO QUEST-- ")
    print("1 - Registrar jugador!")
    print("2 - Consultar datos de jugador!")
    print("3 - Salir")
    try:
        opc = int(input("INgrese su opcion por favor!\n"))

    except:
        print("malito")