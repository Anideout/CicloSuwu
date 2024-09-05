import random, csv
from os import name, system
productos_nombres = ["televisor", "lavadora", "refrigerador", "microondas", "computadora", "celular", "impresora", "cafetera", "licuadora", "ventilador"]
precio_productos = []
registros = []
producto = []
#opcion de limpiar pantalla
def limpiar_pantalla():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():
    limpiar_pantalla()
    print("Analisis de precios de productos\n\n")
    print("1. Asignar precios aleatorios")
    print("2. Clasificar precios")
    print("3. Ver estadistica")
    print("4.Reporte de precios")
    print("5. Borrar archivos")
    print("6. Buscar producto\n")
    print("7. Salir del programa\n")




def obtener_productos():
    limpiar_pantalla()
    for nombre in range(len(productos_nombres)):
        precio = random.randint(300000, 2500000)
        precio_productos.append(precio)
        print(f"Nombre: {productos_nombres[nombre]}, Precio: {precio}\n")

    input("Presione Enter para continuar...\n")

#clasificar precios
def clasificacion_precios():
    limpiar_pantalla()
    for x in range(len(precio_productos)):
    
        if precio_productos[x] < 800000:
            print(f" {productos_nombres[x]} es mas barato: {precio_productos[x]}\n")
        elif precio_productos[x] >= 800000 and precio_productos[x] < 2000000:
            print(f" {productos_nombres[x]} es de precio medio: {precio_productos[x]}\n")
        else:
            print(f" {productos_nombres[x]} es más caro: {precio_productos[x]}\n")
    
    input("Presione Enter para continuar...\n")


#hacer las estradisticas
def obtener_estadistica():
    valor_pequeño = 800000
    valor_grande = 2500000
    ind_peq = 0
    ind_gran = 0
    multi = 1
    mayor_precio = max(precio_productos)
    menor_precio = min(precio_productos)
    promedio = sum(precio_productos) / len(precio_productos)
    print(f"El precio mayor es de ${mayor_precio}\n")
    print(f"El precio menor es de ${menor_precio}\n")
    print(f"EL promedio de los precios es de{promedio}")

    for x in range(len(productos_nombres)):
        if precio_productos[x] < valor_pequeño:
            valor_pequeño = precio_productos[x]
            ind_peq = x
        else:
            None
    print(f"El producto con el precio más pequeño es {productos_nombres[ind_peq]} y su precio es de ${valor_pequeño}\n")
    
    for i in range(len(productos_nombres)):
        if precio_productos[x] <= valor_grande:
            valor_grande = precio_productos[x]
            ind_gran = i
        else:
            None
    print(f"EL producto con el precio más grande es {productos_nombres[ind_gran]} y su precio es de ${mayor_precio}")
    
    for y in range(len(productos_nombres)):
        multi = precio_productos[y] * multi
    geom = (multi) ** (1/10)
    print(f"La media geométrica de todos los precios es de: {geom}")

    
    input("Presione Enter para continuar...\n")

def rep_precios():
    for x in range(len(productos_nombres)):
        prod = productos_nombres[x]
        precio_base = precio_productos[x]
        desc_prom = precio_productos[x] * 0.1
        desc_memb = precio_productos[x] * 0.05
        precio_total = precio_base - desc_prom - desc_memb
        reg_prod = [prod, precio_base, desc_prom, desc_memb, precio_total]
        print(reg_prod)
        input("Presione Enter para continuar...\n")
        registros.append(reg_prod)

    print("Descargar archivo")
    with open('reporte_precios.csv', mode = 'w', newline= '') as file:
        writer = csv.writer(file)
        writer.writerow(["PRODUCTO", "PRECIO BASE","DESCUENTO PROMOCION", "DESCUENTO MEMBRESIA", "PRECIO TOTAL"])
        for y in range(len(productos_nombres)):
            writer.writerow(registros[y])
    
    print("archivo 'reporte_precios.csv' creado exitosamente\n")
    input("Presione Enter para continuar...\n")

def borrar_producto():
    limpiar_pantalla()
    buscar = input("Ingrese el producto que sea eliminar!\n")
    for producto in productos_nombres:
        if producto == buscar:
          productos_nombres.remove(buscar)
    print(productos_nombres)
    input("enter para continuar!\n")


def buscar_producto():
    print(productos_nombres)
    buscar = input("Ingrese el producto que sea buscar!\n")
    for producto in productos_nombres:
        if buscar == producto:
            print(f"PRODUCTO: {producto[0]}")
            print(f"PRECIO: {producto[1]}")
#opcion salir
def salir_menu():
    limpiar_pantalla()
    print("Ha salido del sistema....")
    input("presione enter para continuar")
    


