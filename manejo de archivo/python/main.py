from functions import *


while True:
    menu()

    try:

        opcion = int(input("ingrese opcion\n")) 

        if opcion == 1:
            printt("Registrar Estudiante")

            registrar_estudiante()

        elif opcion == 2:
            printt("Buscar Estudiante")

            mostrar_estudiante()

        elif opcion == 3:
            printt("Imprimir Certificados")

            imprimir_certificados()

        elif opcion == 4:

            descargar_archivo()
            

        elif opcion == 5:
            printt("Salir")

            break

    except:
        printt("opcion ingresada no es valida")