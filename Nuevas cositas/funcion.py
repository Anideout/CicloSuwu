import random, csv, time
from os import system, name

productos = ["Televisor", "Lavadora", "Refrigerador", "Microondas", "Computadora", "Celular", "Impresora", "Cafetera", "Licuadora", "Ventilador"]
precios = []
clasificacion = []
registros = []


def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")
    
def precio_aleatorio():
    
    precio = [random.randint(300000, 2500000) for _ in range(10)]
    precios.append(precio)
    printt(precios)
    time.sleep(2)
    clear()


def class_precios():
    clear() 
    precio1 = 800000
    precio2 = 800000
    precio3 = 2000000
    
    
    #inicializar listas para cada rango de precios 
    rango = []
    rango2 = []
    otros = []

    #clasificar productos segun su precio
    for producto, precio in productos:
        if precio < precio2:
            rango.append((producto, precio))
        elif precio_lmite <= precio <= precio3:
            rango2.append(producto, precio)
        else:
            otros.append(producto, precio)
    

    printt("Productos con precios menores a $800.000:")
    for producto, precio in rango:
        printt(f"{producto}: ${precio}")

    printt("Productos con precios entre $800.000 y $2.000.000")
    for producto, precio in rango2:
        printt(f"{producto}: ${precio}")
    
    if otros:
        printt("\nOtros productos:")
        for producto, precio in otros:
            printt(f"{producto}: {precio}")

    





def menu():
    while True:
        printt("1. Asignar precios aleatorios!")
        printt("2. Clasificar precios!")
        printt("3. Ver estadisticas")
        printt("4. Reporte de precios")
        printt("5. Salir del Programa!")
        try:
            opc = int(input("Ingrese su opcion por favor!\n"))
            if opc == 1:
                clear()
                printt("Asignar precios!\n")
                precio_aleatorio()
            elif opc == 2:
                clear()
                printt("Clasificar precios!\n")
                class_precios()
            elif opc == 3:
                clear()
                printt("ver estadisticias!\n")
                ver_estadisticas()
            elif opc == 4:
                clear()
                printt("Reporte de precios!\n")
            elif opc == 5:
                printt("usted ha salido del sistema...")
                break
            else:
                printt("ingrese una de las opciones por favor!\n")
        except:
            clear() 
            printt("intente de nuevo por favor!\n")
menu()