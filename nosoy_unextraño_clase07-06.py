from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _= system('cls')
    else:
        _ = system('clear')
        
        
    
asientos = []
reservados = []
menu = True

while menu:
    os.system("cls")
    print('Bienvenido a turbus! \n Seleccione su opcion! ')
    print('1. Mostrar asientos disponibles! ') 
    print('2. Reservar asiento! ')
    print('3. Mostrar reservas! ')
    print('4. Salir del sistema... ')
