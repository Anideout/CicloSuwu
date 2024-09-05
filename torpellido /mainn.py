from funcion import *
contado_id=1
banMenu = True
while banMenu:
    menu()
    opc = int(input("Ingrese su opcion por favor! \n"))
    if opc == 1:
        registrar_estudiante()
    elif opc == 2:
        buscar_estudiante()
    elif opc == 3:
        imprimir_certificados()
    elif opc == 4:
        salir()
        banMenu = False
    else:
        print("Opcion ingresada no existe! por favor vuelva a intentarlo")