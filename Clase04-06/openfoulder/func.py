from os import system
from time import sleep
#funcion para limpiar pantalla tanto en windows como en cualquier otro OS 
def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

#Funcion ejercicio 1 
def suma(num1, num2):
    suma = num1 + num2
    return suma

#Funcion ejercicio 2 
def es_par(num1):
    if num1 % 2 == 0:
        print("es par! ")
        return True
    else:
        print("es impar! ")
        return False

#Funcion ejercicio 3 
def celsius_a_fahrenheit(x):
    fah = x*(9/5)+32
    return fah

#Funcion ejercicio 4
def max_de_tres(x,y,z):
    num_mayor = x 
    for n in range(2):
        if y > num_mayor:
            num_mayor = y

        elif z > num_mayor:
            num_mayor = z
    return num_mayor

#Funcion ejercicio 5 
def validar_nombre(nom):
    while nom == "":
        clear()
        nom = input("Vuelva a ingresar su nombre, no debe estar vacío: \n ")
    return nom
    


