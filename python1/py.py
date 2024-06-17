nombres = ["coni", "mati"]

#abrimos en modo escritura! 
archivo = open("dueles.txt", "w")

#recorremos la lista y agregamos los nombres al archivo
for nombre in nombres:
    archivo.write(nombre + "\n")

#importante cerrar el archivo uwu 
archivo.close()