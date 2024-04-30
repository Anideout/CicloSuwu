import time, os
user = "admin"
password = "admin"
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
            while rut <= 5000000 or rut >= 39999999:
                rut = int(input(" ingrese su rut, >= a 5M y =< 39.9M \n"))
            edad = int(input("ingrese edad \n"))
            while edad < 17 or edad >90:
                edad = int(input("ingrese su edad  \n"))
            correo = input("ingrese su correo\n")
            while '@' not in correo:
                correo = input("ingrese su correo\n")
            nem = float(input("ingrese nem\n"))
            
            
        elif opcion == 2:
            os.system("cls")
            print("CONSULTA DATOS ALUMNO")
            username = input("ingrese usuario \n")
            psswrd = input("ingrese password\n")
            if(user == username and password == psswrd):
                rut_alumno = int(input("ingrese rut de alumno a buscar \n"))
                if rut_alumno == rut:
                    print("NOMBRE: ", nombre)
                    print("Direccion: ", direccion)
                    print(f"Edad: {edad}")
                    print("Correo: ", correo)
                    print(f"Nem: {nem}")
                    if nem <= 520:
                        print("CAGASTE")
                    else:
                        print("pasastes :D")
                        
                else:
                    print("el rut ingresado no existe")
                print("pulse tecla para continuar uwu ")
                x = input()
            elif opcion == 3:
                os.system("cls")
                print("SALIR")
            print("Ha salido del sistema")
    except:
        print("opcion no existe pooo ")