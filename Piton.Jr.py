# definicion de variables
nombre = "juan" # string = como caracter
apellido = "perez" # -> String
genero = 'm' #char = se parece a "como caracter de 1 bit"
numero = 3 #int-> integer = se parece a como entero 
numero2 = 3.5 #double-> float -> Se parece a " como real"
flag = True #boolean -> Se parece a "como logico"

#concatenar 
nombrecompleto = nombre + " " + apellido
# enviar info por consola
print(nombrecompleto) # escribir
#enviar info concatenada
print(f"el numero que asignaste es el {numero}")
#solicitar info por consola
raza = input ("ingresa raza de tu mascota")
numero3 = int(input("ingrese numero"))
#numero4 = float(input{"ingresar otro numero"})

# si - entonces
if numero > 10: 
    # ojito con las identaciones
    print("el numero es mayor")
elif numero < 10:
    print("el numero es menor a 10")
elif numero > 10000:
    print("el numero es menor a 10000")
elif numero < 10000:
    print("el numero es mayor a 10000")
    