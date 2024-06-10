import os,time
def Reserva():
    os.system("cls")
    nombre = input("\nIngrese el nombre: ")
    while nombre == "":
        os.system("cls")
        nombre = input("\nIngrese el nombre nuevamente, no debe de estar vacio: ")
    
    os.system("cls")
    banRut = True
    while banRut:
        try:
            rut = int(input("\nIngrese el rut: "))
            banRut = False
        except:
            print("\nRut ingresado no válido. Intente nuevamente.")
            
    