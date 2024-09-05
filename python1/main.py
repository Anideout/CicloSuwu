from functions  import *

banderaMenu = True
while banderaMenu:
        menu_principal()
        try:
            opcion = int(input("Ingrese una opción: \n"))
            if opcion == 1:
                registrar_paciente()
            elif opcion == 2:
                atencion_paciente()
            elif opcion == 3:
                gestionar_paciente()
            elif opcion == 4:
                printt("Ha salido del sistema…")
                input("Presiona Enter para salir...")
                banderaMenu = False
            else:
                printt("Opción no válida.")
        except:
            printt("Opción ingresada no es válida.")