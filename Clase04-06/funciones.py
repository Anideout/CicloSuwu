import os
# Función ejercicio 1
def suma(num1,num2):
    suma = num1 + num2
    return suma

# Función ejercicio 2
def es_par(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False
    
# Función ejercicio 3
def celsius_a_fahrenheit(x):
    fah = x*(9/5)+32
    return fah

# Función ejercicio 4
def max_de_tres(x,y,z):
    num_mayor = x
    for n in range(2):
        if y > num_mayor:
            num_mayor = y
        elif z > num_mayor:
            num_mayor = z
    return num_mayor

# Función ejercicio 5
def validar_nombre(nom):
    while nom == "":
        os.system("clear")
        nom = input("Vuelva a ingresar su nombre, no debe estar vacío: ")
    return nom