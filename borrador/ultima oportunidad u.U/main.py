from funcionn import * 
banderamenu = True


while banderamenu:
    clear()
    menu()
    opc = int(input("Ingrese una de las 5 opc \n"))
    if opc == 1:
        obt_productos()
    elif opc == 2:
        clasificar_precios()
    elif opc == 3:
        obtener_estadisticas()
    elif opc == 4:
        rep_precios()
    elif opc == 5:
        salir_menu()
        banderamenu = False
    else:
        print("nose")