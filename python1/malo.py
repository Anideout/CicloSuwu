from funciones import *
clear()
banMenu = True

while banMenu:
    menu_principal()
    try:
        
        opc = int(input("Ingrese una opcion: \n"))
        if opc == 1:
            clear()
            registrar_paciente()
        elif opc == 2:
            clear()
            atencion_paciente()
        elif opc == 3:
            clear()
            gestionar_paciente()
        elif opc == 4:
            clear()
            printt("Ha salido del sistema... ÑPO21")
            input("Presione enter para salir...")
        else:
            printt("Opcion no valida! ")
    except:
        printt("Opcion ingresada no es valida")