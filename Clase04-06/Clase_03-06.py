# Funcion sin argumento y sin retorno
# Argumento: Valor que se pone dentro del parentesis de la función """

import time, os
def saludar():
    print("Hola")

saludar()


# Funcion sin argumento y con retorno
def despedir():
    mensaje = "Chao"
    # Manda la variable al código, pero no se muestra, ya que no hay un print
    return mensaje

"""
despedir()
# No dará la viarble, se debe poner dentro de un print
print(despedir())
"""

# Se puede asignar a ifs u otras cosas para ver o comparar resultados
if despedir() == "Chao":
    print("Chao Chao")
else:
    print("No entiendo que pasa...")

# Se crea una función con 3 argumentos
"""
def multiplicar(a,b,c):
    resultado = a * b * c
    print(f"El resultado de la multiplicación es: {resultado}")

num1 = int(input("\nIngrese número: "))
num2 = int(input("\nIngrese número: "))
multiplicar(2,num1,num2)
"""
def sexoC_a_sexoS(genero):
    generoS = ""
    while genero != 'f' and genero != 'm':
        os.system("cls")
        genero = input("\nIngrese sexo (m o f): ").lower()
    if genero == 'm':
        generoS = "Masculino"
    else:
        generoS = "Femenino"
    return generoS

generoC = input("\nIngrese sexo: ")
if sexoC_a_sexoS(generoC) == "Masculino":
    print(sexoC_a_sexoS(generoC))
else:
    print("Okay")
