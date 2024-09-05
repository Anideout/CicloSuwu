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
for i in range(40):
    asientos.append(str(i+1))
while menu:
    clear()
    print('\t\tBienvenido a turbus! \n Seleccione su opcion! ')
    print('1. Mostrar asientos disponibles! ') 
    print('2. Reservar asiento! ')
    print('3. Mostrar reservas! ')
    print('4. Salir del sistema... ')
    try:
        opc = int(input('Ingrese una opcion para continuar! '))
        if opc == 1:
            asiento = True
            while asiento:
                clear()
                print("asientos disponibles! ")
                for i in range(40):
                    if i%5 == 0:
                        print(f'{asientos[i]}', end='\t')
                        print(f'{asientos[i+1]}', end='\t')
                        print(f'{asientos[i+2]}', end='\t')
                        print(f'{asientos[i+3]}', end='\t')
                        print(f'{asientos[i+4]}')
                input('\nPresione enter para continuar.... ')
                asiento = False
        elif opc == 2:
            print('Reserve su asiento\n')
            banUsuario = True
            clear()
            banRut = True
            while banRut: 
                try:
                    rut = int(input('Ingrese su rut por favor, no debe contener digito verificador !\n'))
                    if rut >= 5000000  and rut <= 99999999:
                        clear()
                        print('Rut ingresado correctamente! ')
                        banRut = False

                    else:
                        clear()
                        print('RUt ingresado no valido, intente de nuevo! ')


                except:
                    print('rut ingresado no valido! ')
            clear()
            banNombre = True
            while banNombre:
                nombre = input("Ingrese su nombre!\n")
                if nombre != "":
                    print('\nNombre ingresado correctamente! :')
                    banNombre = False
                    clear()
                else:
                    print('\nNombre vacio. intente de nuevo!')
                    clear()

            banDir = True
            while banDir:
                direccion = input('Ingrese su direccion\n')
                if direccion != "":
                    print("direccion registrada!")
                    clear()
                    banDir = False
                    

                else:
                    clear()
                    print("direccion no registrada, intente de nuevo ")
            
            banEdad = True
            while banEdad:
                try:
                    edad = int(input("\nIngrese su edad! "))
                    if edad >= 0 and edad <= 110:
                        clear()
                        print("Edad registrada! ")
                        banEdad = False

                    else:
                        print("edad no ingresada! ")


                        

                except:
                    print("edad no registradA! ")

            clear()
            banCorreo = True
            while banCorreo:
                correo = input("ingrese su correo por favor. Recuerde que debe contener un @ para que sea valido! ")
                if '@' in correo:
                    clear()
                    print("\ncorreo registrado!")
                    banCorreo = False
                    time.sleep(1)
                else:
                    clear()
                    print("\nCorreo no valido. Intente nuevamente agregando @ esta vez! ")
                    


            

                

            


    except:
        print("opcion ingresad no valida! ")