# funcion para limpiar pantalla XD
from os import system, name
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

# declaracion de listas
asientos = []
comprados = []

# llenar asientos con numeros del 1 al 24
for i in range(24):
	asientos.append(str(i+1)) # str() convierte a string


# L0OOP PRINCIPAL

while True:
	# imprimir asientos disponibles
	clear()
	print('asientos disponibles:\n')
	for i in range(24):
		# if i%4 == 0 --> 'si el numero es multiplo de 4'
		# solo hago esto para imprimir 4 items en la lista de asientos por linea
		if i%4 == 0:
			# end='\t' termina el print con un tab en vez de linea nueva
			print(f'{asientos[i]}', end='\t') 
			print(f'{asientos[i+1]}', end='\t')
			print(f'{asientos[i+2]}', end='\t')
			print(f'{asientos[i+3]}')


	resp = input('\nelige un asiento (o \'q\' para salir, \'v\' para ver sus asientos comprados): ')
	
	if resp in asientos and resp is not 'x' and resp is not 'X':
		asientos[int(resp)-1] = 'X' # int() convierte a numero entero
		comprados.append(resp) # el asiento comprado se almacena en la lista de comprados
		clear()
		input(f'se ha comprado el asiento {resp}.\npresione enter para continuar...')
	# lower() convierte a minuscula y con "elif resp.lower() is 'v'"
	# tendria q haber sido suficiente pero no me quizo pescar python XD
	elif resp is 'v' or resp is 'V':
		clear()
		# if not lista -> 'si la lista esta vacia'
		if not comprados:
			print('no ha comprado ningun asiento')
		else:
			print('usted ha comprado los siguientes asientos:',end=' ')
			for i in comprados:
				print(i,end='\t')
		input('\n\npresione enter para continuar...')

	# para salir del programa
		exit(0)


	else:
		clear()
		input('respuesta invalida o asiento ya esta comprado (\'X\')\npresione enter para continuar...')
		