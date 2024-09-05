import time, os
os.system("cls")
menu = True


while menu:
    print("\nBienvenido al centro medico del DUOC! ")
    print("1. Registrar paciente ")
    print("2. Atencion al cliente")
    print("3. Consultar datos paciente")
    print("4. salir")
    try:
        opc = int(input("Ingrese una opcion!:\n "))
        if opc == 1:
            os.system("cls")
            print("\n----- Registro de paciente -----")
            
            
            banRut = True
            while banRut:
                try:
                    rut = int(input("Ingrese su rut (Sin digito verificador ni puntos por favor uwu)\n"))
                    if rut >= 5000000 and rut <= 99999999:
                        print("\n Rut registrado!")
                        banRut = False
                    else:
                        os.system("cls")
                        print("\nHa ingresado un rut no válido, intente nuevamente porfavor. ")
                        
                except:
                    os.system("cls")
                    print("\nRut no válido, por favor intente nuevamente (Entre 5000000 y 99999999)")
                    
                    
            nombre = ""
            nombre = input("\ningrese su nombre porfavor uwu\n")
            while nombre == "" and nombre == " ":
                nombre = input("ingrese su nombre nuevamente porfavor uwu")
                
            direc = ""
            direc = input("\ningrese su direccion porfavor uwu\n")
            while direc == "" and direc == " ":
                direc = input("ingrese su direccion nuevamente porfavor uwu")
                
            correo = input("\n ingrese su correo porfavor (debe contener un @):\n")
            while '@' not in correo:
                correo = input("\ningrese su correo nuevamente, recuerde que debe contener un @: ")
                
                
            try:
                BanderaEdad = True
                while BanderaEdad:
                    edad = int(input("ingrese edad: (De 18 a 120)\n"))
                    if edad > 17 and edad < 111:
                        print("Edad registrada exitosamente!!!!")
                        BanderaEdad = False
                        os.system("cls")
                    else:
                        os.system("cls")
                        print("\nLa edad no es válida, intente nuevamente.\n")
            except:
                print("\nLa edad no es válida, intente con números enteros.")
                
            try:
                banderaGENERO = True
                while banderaGENERO:
                    genero = input("ingrese su genero por favor, indique con un M o una F, y bueno tb con O si se considera no binarie uwu\n")
                    if genero == "M" or genero == "F" or genero == "m" or genero == "f" or genero == "O" or genero == "o":
                        print("genero registrado exitosamenet!!! ")
                        banderaGENERO = False
                        
                    else:
                        os.system("cls")
                        print("\n opcion no valida! por favor indique su genero con las siglas (M, F, O)")
            
            
            except:
                print("opcion no valida")
            try:
                banderaPS = True
                while banderaPS:
                    ps = input("Por favor indique cual es su PS:   1) ISAPRE   2) FONASA \n")
                    if ps == "ISAPRE" or ps == "FONASA" or ps == "isapre" or ps == "fonasa": 
                        print("PS registrada exitosamente!")
                        banderaPS = False
                        os.system("cls")
                        
                    else:
                        os.system("cls")
                        print("\nOpcion no valida! recuerde que tiene que indicar con (ISAPRE y FONASA), intente nuevamente! ")
            except:
                print("\nopcion no valida! por favor ingrese de nuevo ")
                
        elif opc == 2:
            os.system("cls")
            print("\n --------- Atencion al Paciente! ------------")
            try:
                compr_rut = int(input("\nIngrese el rut del paciente (sin Dígito verificador ni puntos por favor uwu )"))
                if compr_rut == rut:
                    os.system("cls")
                    print("\nPaciente encontrado!")
                    
                    fecha = input("\nIngrese la fecha de la visita del paciente: ")
                    
                    obs = input("\nEscriba las observaciones del paciente:\n")
                else:
                    os.system("cls")
                    print("\nEl paciente no se ha encontrado, intente otro rut.")
            except:
                print("\n El rut ingresado no es válido. Intente nuevamente.")
                
                
        elif opc == 3:
            os.system("cls")
            try:
                cons_rut = int(input("ingrese su rut por favoreee "))
                if cons_rut == rut:
                    
                
                
                    print("\n------ Datos Paciente ------")
                    print(f"Nombre del paciente: {nombre}")
                    print(f"Rut del paciente: {rut}")
                    print(f"edad del paciente : {edad} años")
                    print(f"Genero de paciente : {genero}")    
                    print(f"Dirección del paciente: {direc}")
                    print(f"Correo del paciente: {correo}")
                    print(f" Plan de salud del paciente: {ps}")
                    print(f"Fecha de la visita: {fecha}")
                    print(f"Observaciones: {obs}")
                    time.sleep(4)
                    os.system("cls")
                else:
                    print("\nEl rut ingresado no esta en el sistema. Intente con otro rut ")
            
            except:
                print("\nEl rut ingresado no es válido. Intente nuevamente.")
                
        elif opc == 4:
            print("\nGracias por usar nuestros servicios uwu")
            time.sleep(2)
            menu = False
            os.system("cls")
                    
                
                
            
                
    except:
        print("\ningrese una opcion valida uwu\n") 
        time.sleep(2)
        os.system("cls")