import os,time


banMenu = True

while banMenu:
    printt("*******************************")
    printt("------ Opciones de menú -------")
    printt("1) Reservar asientos")
    printt("2) Mostrar asientos")
    printt("3) Mostrar reservas")
    printt("4) Salir")

    try:

        opc1 = int(input("\nIngrese opción: "))
        

    except:
        printt("Opción de menu no válida. Intente nuevamente.")