lista = [] #variable de lista xd 
#Por cada item (i) en range (3), repita el siguiente codig0#
#range (3) => rango de nyumeros del 0 al 2, por lo que se repite 3 veces
#en cada iteracion, i equivale al numero actual de range()
for i in range(3):

#append() => añade item al final de la lista
# input() => directamente devuelve el termino dado por el uso de {variable}, en este caso i
#la f antes de las comillas permite el uso de {variable}, en este caso i 
# como i empieza en 0 y no 1, lo hago i+1 para que no diga  "numero 0"
    lista.append(input(f'Introduzca el nombre numero {i+1}: \n'))
#max() => devuelve el termino mas largo o numero mas grande
# ejemplo: max([1, 6, 2]) te devuelve el 6 
#para sacar la variable string(texto) mas largo, le das
# la lista y como parametro extra le pones key=len
#len en general significa el largo de un string
#y \n adentro de un string es solo una linea en blanco XD
mas_largo = max(lista, key=len)
print(f'El nombre más largo es: {mas_largo}')