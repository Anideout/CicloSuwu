import random, csv
from os import system, name
productos = [
    "Televisor",
    "Lavadora",
    "Refrigerador",
    "Microondas",
    "Computadora",
    "Celular",
    "Impresora",
    "Cafetera",
    "Licuadora",
    "Ventilador"
]
precios = []
clasificacion = []
registros = []




def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")


def menu():
    print("\t\tAnalisis de precios de productos\n")
    print("1- Asignar precios aleatorios\n")
    print("2- Clasificar precios!\n")
    print("3- Ver estadisticas!\n")
    print("4- Reporte de precios\n")
    print("5- Salir\n")
    

def obtener_productos():
    clear()
    for nombre in range(len(productos)):
        precio = random.randint(300000, 2500000)
        precios.append(precio)
        print(f"producto: {productos[nombre]}. Precio: {precio}\n")

    input("Presione enter para continuar\n")



#clasificar precios
def clasificar_precios():
    clear()
    for x in range(len(precios)):
        if precios[x] < 800000:
            print(f"{productos[x]} es mas barato: {precios[x]}\n")
        elif precios[x] >= 800000 and precios[x] < 2000000:
            print(f" {productos[x]} es de precio medio:{precios[x]}")
        else:
            print(f"{productos[x]} es más caro con un precio de {precios[x]}\n")
    input("Enter para continuar!\n")

def obtener_estadisticas():
    valor_pequeño = 2500000
    ind_peq = 0 
    multi = 1
    mayor_precio = max(precios)
    menor_precio = min(precios)
    promedio = sum(precios) / len(precios)
    print(f"El precio mayor es de ${mayor_precio}\n")
    print(f"El precio menor es de ${menor_precio}\n")
    print(f"El promedio de precios es de {promedio}")

    for x in range(len(productos)):
        if precios[x] < valor_pequeño:
            valor_pequeño = precios[x]
            ind_peq = x
        else:
            None
    print(f"El producto con el precio más pequeño es {productos[ind_peq]} y su precio es de ${valor_pequeño}\n")

    for y in range(len(productos)):
        multi = precios[y] * multi
    geom = (multi)** (1/10)
    print(f"La media geometrica de todos los precios es de: {geom}\n")

    input("Enter para continuar\n")

def rep_precios():
    for x in range(len(productos)):
        prod = productos[x]
        precio_base = precio_productos[x]
        descuento_promo = precios[x] * 0.1
        descuento_memb = precios[x] * 0.05
        precio_total = precio_base - descuento_promo - descuento_memb
        reg_prod = [prod, precio_base, descuento_promo, descuento_memb, precio_total]
        print(reg_prod)
        input("Enter para continuar!\n")
        registros.append(reg_prod)

    print("Descargar archivo\n")
    with open('reporte_precios.csv', mode = 'w', newline= '') as file:
        writer = csv.writer(file)
        writer.writerow(["PRODUCTO", "PRECIO BASE", "DESCUENTO PROMOCION", "DESCUENTO MEMBRESIA", "PRECIO TOTAL"])
        for y in range(len(productos)):
            writer.writerow(registros[y])
    
    print("Archivo 'reporte_precios.csv' creado con exito!\n")
    input("Presione enter para continuar\n")


def salir_menu():
    clear()
    print("Ha salido del sistema....")
    input("Presione enter para continuar\n")

