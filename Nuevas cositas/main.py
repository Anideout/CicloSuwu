from funcion import *

while True:
    menu()
    opc = int(input("Ingrese su opcion!\n"))
    if opc == 1:
        precio_aleatorio()

    elif opc == 2:
        clasificar_precios()
    elif opc == 3:
        mostrar_productos()
