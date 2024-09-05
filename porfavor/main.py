from funcion import * 

banderamenu = True
while banderamenu:
    clear()
    menu()
    opc = int(input("Ingrese su opcion por favor\n"))
    if opc == 1:
        printt("Asignar sueldos aleatorios!\n")
        sueldos_aleatorios()
    elif opc == 2:
        printt("Clasificar sueldos")
        clasificar_sueldos()
    elif opc == 3:
        printt("Ver estadisticas")
        ver_estadisticas()
       
    elif opc == 4:
        reporte_sueldos()
    elif opc == 5:
        salir_menu()
        banderamenu = False
