import random, json
productos = []



def precio_aleatorio():
    producto = ["Televisor", "Lavadora", "Refrigerador", "Microondas", "Computadora", "Celular", "Impresora", "Cafetera", "Licuadora", "Ventilador"]
    for producto in range(10):
        precio = producto = random.randint(300000, 2500000)
        productos.append(producto)
    printt("precio realizado con exito!\n")
    return precio
    


def clasificar_precios():
    printt("Productos clasificados por precios!:\n")
    printt("---------------------------------------")
    printt("Precios menores a 800.000\n")
    for producto in productos:
        if producto["Televisor"] > 300000 :
            printt(f" TELEVISOR: {producto[0]}")


# Ejemplo de uso



def mostrar_productos():
    productoss = {

    (f"Televisor: $ {random.randint(300000, 2500000)}"),
    (f"Lavadora: ${random.randint(300000, 2500000)}"),
    (f"Refrigerador: ${random.randint(300000, 2500000)}"),
    (f"Microondas: ${random.randint(300000, 2500000)}"),
    (f"Computadora: ${random.randint(300000, 2500000)}"),
    (f"Celular: ${random.randint(300000, 2500000)}"),
}
    printt(productoss)



def menu():
    printt("1. Precios aleatorios")
    printt("2. Clasificar precios!")
    printt("3. Mostrar productos")