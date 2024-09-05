from func import *
from os import system, name
import time
def clear(): #ESTO LO HAGO BASICAMENTE PARA LIMPIAR PANTALLA TANTO EN WINDOWS COMO EN CUALKIER OS xd
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
#ejercicio 1 
clear()
banSuma = True #se crea una bandera, para que cumpla la condicion boleana (true o false)
while banSuma:
    try:
        num1 = int(input("Ingrese su primer numero!:  \n")) #te pide ingresar el primer numero
        num2 = int(input("Ingrese su segundo numero!: \n ")) #te pide ingresar el 2do numero
        banSuma = False
        #aqui se ingresa la bandera para terminar el bucle, en caso de no cumplir la condicion, que en este caso es no ingresar numeros enteros, le imprimira el mensaje de "except" y ahí te devuelve en el bucle 

    except: #en caso de no cumplir la condicion de int(enteros) te tira a except, pidiendote que lo vuelvas a intentar 
        clear() #para limpiar la pantalla XD
        printt("Usted ha ingresado un valor no válido. intente de nuevo ! ")
clear()
printt("la suma de sus numeros es:", suma(num1,num2)) #se imprime el resultado, el suma() que es la funcion, y las variables num1, num2
time.sleep(2)

#ejercicio 2 
clear()
banPar = True
while banPar:
    try:
        num1 = int(input("\nIngrese su número: \n"))
        banPar = False
    except:
        clear()
        printt('Usted a ingresar un valor no valido, intente nuevamente!!! ')
clear()
printt(es_par(num1))
time.sleep(2)

#Ejercicio 3 
clear()
banFah = True
while banFah:
    try:
        temp = int(input("INgrese su temperatura! (en °C):\n"))
        banFah = False
    except:
        printt("Usted ha ingresado un valor no valido, intente de nuevo por favor ! ")

clear()
printt('su temperatura en a grados fahrenheit es',celsius_a_fahrenheit(temp))
time.sleep(2)

#ejercicio 3 
clear()
banMax = True
while banMax:
    try:
        num1 = int(input("\nIngrese su primer numero! : \n"))
        num2 = int(input("\nIngrese su segundo numero!: "))
        num3 = int(input("\nIngrese su tercer numero!: ")) 
        banMax = False


    except:
        clear()
        printt("usted ha ingresado un valor no valido, recuerde que tiene que ser numeros enteros! ")

clear()
printt(max_de_tres(num1,num2,num3))
time.sleep(2)

#ejercicio 4 
clear()
nombre = input("\nIngrese su nombre! ")
clear()
printt(validar_nombre(nombre))
time.sleep(2)
