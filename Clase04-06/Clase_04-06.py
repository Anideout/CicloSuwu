from funciones import *

import os, time


# Ejercicio 1

os.system("clear")

banSuma = True

while banSuma:

    try:

        num1 = int(input("\nIngrese su primer número: "))

        num2 = int(input("\nIngrese su segundo número: "))

        banSuma = False

    except:

        os.system("clear")
        printt("Usted a ingresado un valor no válido. Intente nuevamente.")


os.system("clear")
printt(suma(num1,num2))

time.sleep(2)


# Ejercicio 2

os.system("clear")

banPar = True

while banPar:

    try:

        num1 = int(input("\nIngrese su número: "))

        banPar = False

    except:
        printt("Usted a ingresado un valor no válido. Intente nuevamente.")


os.system("clear")
printt(es_par(num1))

time.sleep(2)


# Ejercicio 3

os.system("clear")

banFah = True

while banFah:

    try:

        temp = int(input("\nIngrese su temperatura (En °C): "))

        banFah = False

    except:

        os.system("clear")
        printt("Usted a ingresado un valor no válido. Intente nuevamente.")
        

os.system("clear")
printt(celsius_a_fahrenheit(temp))

time.sleep(2)


# Ejercicio 4

os.system("clear")

banMax = True

while banMax:

    try:

        num1 = int(input("\nIngrese su primer número: "))

        num2 = int(input("\nIngrese su segundo número: "))

        num3 = int(input("\nIngrese su tercer número: "))

        banMax = False

    except:

        os.system("clear")
        printt("Usted a ingresado un valor no válido. Intente nuevamente.")
        

os.system("clear")
printt(max_de_tres(num1,num2,num3))

time.sleep(2)


# Ejercicio 5

os.system("clear")

nombre = input("\nIngrese su nombre: ")

os.system("clear")
printt(validar_nombre(nombre))

time.sleep(2)