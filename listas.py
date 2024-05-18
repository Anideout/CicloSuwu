numeros = [0, 3, 5, 4, 2]
#Que hacen estas funciones??
"""
BBDD: Data Modeler
Programación: Java de Escritorio
"""

numeros = [1,2,3,4,5,6,7,8,9,0]
# Lo que esta dentro de una lista son los "Elementos" de la lista
# Las posiciones de los números son "Indices", empieza siempre desde el 0


# Imprime el número que este en la posición 0 de la lista
# print(numeros[0])

# Imprime el largo de la lista numeros
# print(len(numeros)) 

# Agrega a la lista números el número 6, al no tener una posición asignada, se agrega al final de la lista
# numeros.append(6)

# Inserta el número 7 en el índice 2 de la lista, sin borrar el número de la lista, desplaza los números al siguiente indice
# numeros.insert(2, 7)

# Elimina el primer elemento 5 de la lista
# numeros.remove(5)

# Saca de la lista el elemento que se encuentre en el índice 1
# numeros.pop(1)

# Limpia la lista de todos los elementos que estan en ella.
# numeros.clear()

# Te imprime el indice del número 5
# print(numeros.index(5))
 
# Devuelve las veces que aparece el número 4 en la lista
# print(numeros.count(4)) 

# Ordena la lista de menor a mayor
# numeros.sort()
# print(numeros) 

# Invierte la lista, moviendo los datos que estaban al inicio para el final y viceversa
# numeros.reverse()

# Copia la lista que uno desee y la guarda en una nueva variable
# numeros_copy = numeros.copy()
# print(numeros_copy)  

# Se le asigna a la variable otra_lista los números 7 y 8. Luego a la variable "concatenada" se le agregan los números de la lista 'numeros' y la lista 'otra_lista'
# Luego se imprime para ver la nueva lista creada.
# En este caso, se suma primero la lista numeros y luego otra_lista, por lo que el orden es ese.
# otra_lista = [7, 8]
# concatenada = numeros + otra_lista
# print(concatenada)  

# En la variable 'repetida' se multiplica la lista por 2, dando como resultado una lista con los mismos valores 2 veces.
# En otras palabras, la variable contiene los elementos de la lista 'numeros' 2 veces, es similar a hacer: repetida = numeros + numeros
# repetida = numeros * 2
# print(repetida)  