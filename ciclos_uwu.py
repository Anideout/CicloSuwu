#ejercicio 1. calcula la factorial de un numero :333 
# numero=int(input("Ingrese un numero :D "))
# factorial=1 #por que 1? pq haremos una multiplicacion uwu y como todo numero multiplicado en 0 da 0, tiene que ser del 1 en adelante uwu~
# if numero!=0:
#     for i in range(1,numero+1):
#         factorial =factorial *i 
# # print("la factorial seria uwu : ", factoria

#ejercicio 2 

# while True :
#     num = int(input("ingrese un numero we \n"))
#     if(num%2==0):
#         print ("ERROR AYUDAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ")
#         continue
#     else:
#         (print(f"el numero ingresado es par :D "))
#         result = num * 4
#         print(F"el numero {num} multiplicado por 4 es: {result}")
#         break
# resultado = 1
# base =int(input("ingrese una base uwu \n"))
# exponente =int(input("ingrese exponente \n"))
# for i in range(exponente):
#     resultado = resultado * base
# print(f"el resultado de {base} elevado a {exponente} es: {resultado}")

def es_primo(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n !=0:
        return es_primo(num, n + 1)
    else:
        print("No es primo u.u", )


    
    