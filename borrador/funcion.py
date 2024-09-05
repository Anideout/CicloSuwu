-# #funcion sin argumento y sin retorno 
import os, time
os.system("cls")
def saludar():
    print("\nHola mundo uwu ")
    
    
#funcion sin argumento y con retorno 


def despedir():
    mensaje = input("dime chau \n")
    return mensaje

saludar()
if despedir() == "chau":
    print("xau xau uwu ")
else:
    print("\tno caxo nada washito :/")
    
#funcion con argumento y sin retorno 

def multiplicar(a, b, c ):
    resultado = a * b * c
    
    print(f"el resultado de la multiplicacion es: {resultado}")
num= int(input("Ingrese numero por favor ! \n"))



multiplicar(2, 4, num)

#funcion con argumento y con retorno
def sexoC_a_sexoS(genero):
    while genero.upper() != 'f' and genero.upper() != 'm':
        genero = input("Ingrese sexo m o f")
    if genero == 'm':
        generoS = "masculino"
    else:
        generoS = "femenino"
    return generoS

generoC = input("ingrese su preferencia sexual!\n ").lower()
print(sexoC_a_sexoS(generoC))
if sexoC_a_sexoS(generoC)  == "Masculino!":
    print(sexoC_a_sexoS)


