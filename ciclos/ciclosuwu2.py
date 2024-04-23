import time
#actividad 2
#ejercicio 1 
contadorProductos = 0
acumuladorPrecio = 0
opcion = int(input("desea llevar agua por $600  1.si    2.no\n"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 600
opcion = int(input("desea llevar azucar por $1200?    1.si     2.no\n"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 1200
opcion = int(input("desea llevar aceite por $1500?    1.si     2.no\n"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 1500
opcion = int(input("desea llevar arroz por $1250?      1.si     2.no\n"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 1250
opcion = int(input("desea llevar fideos por $790?      1.si     2.no\n"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 790
opcion = int(input("desea llevar bebida por $1780      1.si     2.no\n"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 1780
opcion = int(input("desea llevar chocolate $2500      1.si     2.no\n"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 2500
opcion = int(input("desea llevar pan de molde por $1340     1.si     2.no\n"))

print(f"cantidad de productos: {contadorProductos}")
print(f"total provisorio: ${acumuladorPrecio}")
preferencial = int(input("es acaso usted un cliente preferencial?    1.si uwu   2.no unu\n"))
if preferencial == 1:
    total = acumuladorPrecio
    descuento = acumuladorPrecio * 0.25
else:
    total = acumuladorPrecio
    descuento = 0
print(f"descuento: ${descuento}")
print(f"total a pagar: ${total}")
pago = int(input("ingrese una forma de pago 1.efectivo   2. credito/debito\n"))
if pago == 1:
    efectivo = int(input("ingrese valor efectivo"))
    if efectivo < total:
        print("saldo insuficiente, cagaste")
    else:
        vuelto = efectivo - total
        print("muchas gracias uwu ")
        print(f"su vuelto es: ${vuelto}")
else:
    print("no olvide llevar su voucher ")