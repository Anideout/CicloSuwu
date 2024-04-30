import time, os



while True:
    os.system("cls")
    print("\t\tsistema de gestion de alumnos")
    print("1. Registrar alumno")
    print("2. consultar datos de alumnos")
    print("3. Salir")
    try:
        opcion = int(input("ingrese una opcion uwu \n"))
        if opcion == 1:
            os.system("cls")
            print("registro de alumno")
            nombre = input("ingrese su nombre, no acepta cadena vacía \n")
            while nombre == "":
                nombre = input("ingrese su nombre, no acepta cadena vacia u.u \n")
            direccion = input("ingrese su direccion\n")
            while direccion == "":
                direccion = input("ingrese su direccion, no acepta cadena vacia u.u \n")
            edad = int(input("ingrese edad \n"))
        elif opcion == 2:
            print("CONSULTA DATOS ALUMNO")
            x = input()
        
    except:
        print("opcion no existe pooo ")