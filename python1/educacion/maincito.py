from funcction import *

while True:
    menu()
    try:
        opc = int(input("Ingrese su opcion!\n"))
        if opc == 1:
            registrar_alumno()
        elif opc == 2:
            buscar_alumno()
        elif opc == 3:
            print("aun no listo.. .")    
        elif opc == 4:
            print("\nUsted ha salido del sistema....")
        else:
            print("Opcion ingresada no valida... intente de nuevo por favor! ")
            
            
        
        
    except:
        print("Opcion invalida, por favor intente de nuevo! ")
    