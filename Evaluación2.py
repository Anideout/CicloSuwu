#repaso evaluación 2
#recrear un menu
#opcion tiene que registrar un alumno
#validar todos los campos
#opcion 2 tengo que ver el resumen de la ficha




import os
while True:
    print("\t\tSistema de Gestión de Alumnos")
    print("1._ registrar alumno")
    print("2._ consultar datos de alumno")
    print("3._ Salir")
    try:
        opcion = int(input("ingrese una opcion \n"))
        if opcion == 1:
            os.system("cls")
            print("registro de alumno")
            #solicitar nombre y validar que no venga vacio
            nombre = input("ingrese el nombre \n")
            while nombre == "":
                nombre = input("ingrese su nombre, no acepta cadena vacia \n")
            #solicitar dirección y validar que no venga vacia
            dirección = int(input("ingrese dirección \n"))
            while dirección == "":
                dirección = input("ingrese su dirección, no acepta cadena vacia \n") 
            #solicitar el rut y que este entre el rango de 500000 y 39999999. 
            rut = int(input("ingrese su rut \n"))
            while rut <= 5000000 or  rut >= 39999999:
                rut = int(input("ingrese su rut, >= a 5m. y =< a 39 m. \n"))
            #solicitar 
            edad= int(input("ingrese edad \n"))
        elif opcion == 2:
            print()    
        
    except:
        print("opcion invalida")