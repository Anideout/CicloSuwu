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
for i in range(40): #Llenar asientos con numeros del 1 al 40 
                asientos.append(str(i+1)) #str convierte a string
while menu:
    clear()
    print('\t\tBienvenido a turbus! \n Seleccione su opcion! ')
    print('1. Mostrar asientos disponibles! ') 
    print('2. Reservar asiento! ')
    print('3. Mostrar reservas! ')
    print('4. Salir del sistema... ')
    try:
        opc = int(input("\tingrese una opcion para continuar! \n"))
        if opc == 1:
            asiento = True
            while asiento:
                clear()
                print("asientos disponibles\n")
                for i in range(40):
                    if i%5 == 0: #esto es para que imprima 5 items de la lista de asientos por linea 
                                    #end= '\t' termina el print con un tab en vez de linea nueva 
                        print(f'{asientos[i]}', end='\t')
                        print(f'{asientos[i+1]}', end='\t')
                        print(f'{asientos[i+2]}', end='\t')
                        print(f'{asientos[i+3]}', end='\t')
                        print(f'{asientos[i+4]}')
                        
                input('\nPresione enter para continuar...')
                asiento= False

        elif opc == 2:
            print('Reserve su asiento!\n')
            bandUsuario = True
            clear()
            banrut = True
            while banrut:
                try:
                    rut = int(input('Ingrese su rut sin digito verificador por favor!\n'))
                    if rut >= 5000000 and rut <= 99999999:
                        clear()
                        print('Rut ingresado correctamente!')
                        banrut = False
                    else:
                        clear()
                        print('Rut ingresado no valido! recuerde NO ingresar el digito verificador')


                except:
                    clear()
                    print('Rut  invalido! ')
            # Nombre del usuario
            clear()
            banNombre = True
            while bandNombre:
                nombre = input('\nIngrese su nombre!: \n')
                if nombre != "":
                    clear()
                    print('\nNombre registrado!')
                    banNombre = False
                else:
                    clear()
                    print('\nNombre vacío. Intente de nuevo!')
            # Correo usuario 
            banDir = True
            while banDir:
                direccion = input('\nIngrese su direccion!\n')
                if direccion != "":
                    clear()
                    print('\nDireccion registrado!')                    
                    banDir = False

                else:
                    clear()
                    print('\nDireccion vacia. Intente denuevo! ')

                
            #Edad usuario
            clear()
            banEdad = True
            while banEdad:
                try:
                    edad = int(input("\nIngrese su edad! (Debe estar entre 1 a 110)"))
                    if edad >= 0 and edad <= 110:
                        clear()
                        print('\nEdad registrada! ')
                        banEdad = False

                    else:
                        clear()
                        print('\nEdad no valida. intente con numero entero por favor ! ')
                except:
                    print("edad no registrada! intente de nuevo! ")
            #seleccione asiento!
            clear()
            print("Seleccione un asiento disponible!")
            for i in range(0, 40, 5):
                print(f'{asientos[i]}', end='\t')
                print(f'{asientos[i+1]}', end='\t')
                print(f'{asientos[i+2]}', end='\t')
                print(f'{asientos[i+3]}', end='\t')
                print(f'{asientos[i+4]}')
            asiento_seleccionado = input('\nIngrese el numero del asiento!')
            if asiento_seleccionado in asientos:
                asientos.remove(asiento_seleccionado)
                reservados.append({
                    "rut": rutt,
                    "nombre": nombre,
                    "direccion": direccion,
                    "edad": edad,
                    "asiento": asiento_seleccionado
                })
                clear()
                print("\nAsiento reservado con exito!")
            else:
                clear()
                print("\nAsiento no disponib")

    except:
        print("opcion invalida! intente de nuevo ! ")