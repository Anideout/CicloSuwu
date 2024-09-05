from funcions import *
banderaMenu =True
while banderaMenu:
    try:
        menu()
        opcion = int(input("ingrese una de las 5 opciones\n"))
        if opcion == 1:
            obtener_productos()
        elif opcion == 2:
            clasificacion_precios()
        elif opcion == 3:
            obtener_estadistica()
        elif opcion == 4:
            rep_precios()
        elif opcion == 5:
            borrar_producto()
        elif opcion == 6:
            buscar_producto()
        elif opcion == 7:
            salir_menu()
            banderaMenu = False
        else:
            print("nose")
    except:
        print("por favor hagalo bn ")