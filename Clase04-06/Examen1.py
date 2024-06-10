import os,time

banMenu = True
while banMenu:
    print("*******************************")
    print("------ Opciones de menú -------")
    print("1) Reservar asientos")
    print("2) Mostrar asientos")
    print("3) Mostrar reservas")
    print("4) Salir")
    try:
        opc1 = int(input("\nIngrese opción: "))
        
    except:
        print("Opción de menu no válida. Intente nuevamente.")