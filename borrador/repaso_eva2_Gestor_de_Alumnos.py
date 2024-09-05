import time, os
user = "admin"
contra = "1234"

menu = True
os.system("cls")
while menu:
    print("------Bienvenido al sistema de  gestor de alumnos!!!!--------")
    print("1. Registrar usuario! ")
    print("2. Consultar datos de alumnos")
    print("3. Salir")
    
    opc = int(input("ingrese una opcion! \n"))
    try:
        os.system("cls")
        if opc == 1:
            print("Registrar alumno!")
            
            nombre = input("ingrese su nombre por favor \n")
            while nombre == "" or nombre == " ":
                nombre = input("\ningrese su nombre por favor uwu no puede quedar el espacio en blanco!!!!! \n")
                
            direc = input("ingrese su direccion por favor uwu no puede quedar el espacio en blanco!!!!!!! \n")
            while direc == "" or direc == " ":
                direc = input("\ningrese la direccion po  \n")
                    
            banRut = True
            while banRut:
                os.system("cls")
                try:
                    rut = int(input("ingrese su rut por favor uwu, \n"))
                    if rut >= 5000000 or rut <= 39999999:
                        print("rut registrado correctamente ! ")
                        banRut = False
                        time.sleep (2)
                        
                except:
                    print("rut ingresado no valido u.u recuerda NO ingresar el digito verificador y tampoco puntos por la mierda oh ")
                        
            banEdad = True
            while banEdad:
                os.system("cls")
                try:
                    edad = int(input("\nIngrese su edad (De 18 a 120): "))
                    if edad > 17 and edad <= 90:
                        print("\n¡Edad registrada exitosamente!")
                        banEdad = False
                        
                    else:
                        os.system("cls")
                        print("\nLa edad no es válida, intente nuevamente.")
                except:
                    print("rut ingresado no valido, recuerda que no tienes que ingresar el digit verificador ni puntos uwu ")
                    
                
            correo = input("\ningrese su correo electronico por favor uwu \n")
            while '@' not in correo:
                correo = input("ingrese correo correctamente porfavor, si ya te dije que tiene que llevar un @ loco para. \n")
            banNem = True
            while banNem:
                try:
                    nem = float(input("ingrese su nem uwu \n"))
                    while nem:
                        nem = float(input("ingrese su nem correctamente, no sea pao \n"))
                        print("nem registrado con exito uwu")
                        time.sleep(3)
                        os.system("cls")
                        continue
                except:
                    print("nem ingresado no valido, yapo si no es tan dificil tampoco xd ")
                    
                    
    
        elif opc == 2:
            print ("Consultar datos de alumnos ! ")
            user = input("por favor ingrese su nombre de usuario!: \n")
            contra = input("por favor ingrese su contraseña!: \n")
            while user == user and contra == contra:
                print("usuario y contraseña correctos uwu")
                print("Bienvenido adminstrador <3 ")
                time.sleep(3)
                os.system("cls")
                break
            
            banrut2 = True
            while banrut2:
                os.system("cls")
                try:
                    rutt = int(input("ingrese el rut del alumno por favor uwu: \n"))
                    if rutt == rut:
                        print("datos del alumno: ")
                        print("nombre: ", {nombre})
                        print("direccion: ", {direc})
                        print("rut: ", {rut})
                        print("edad: ", {edad})
                        print("correo: ", correo)
                        print("nem: ", {nem})
                        time.sleep(3)
                        os.system("cls")
                        break
                    
                    
                except:
                    print("el rut ingresado no esta validado en el sistema :( intente nuevamente ")
            
            
            
            
                
    
    
    
    
    
    except:
        print("opcion ingresada no valida ")
        