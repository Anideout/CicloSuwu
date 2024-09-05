from funcion_school import *
bandMENU = True
while True:
    imprimir_menu()
    try:
        opcion = int(input("ingrese opcion\n"))
        if opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            buscar_estudiante()
        elif opcion == 3:
            imprimir_certificado()
        elif opcion == 4:
            salir()
            bandMENU = False
        else:
            print("Opcion del menu no valida")
    except:
        print("opcion ingresada no existe")