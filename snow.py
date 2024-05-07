import time, os 
admin = "Admin"
passAdmin = "1234"
while True:
    os.system("cls")
    print("\t\tBienvenido al Hotel Paradise Dreams!!!!!!!!!")
    print("1. Registrar Huésped uwu")
    print("2. Consultar datos de Huésped!")
    print("3. Salir unu")
    try:
        os.system("cls")
        opcion = int(input("ingrese una opcion >.< \n"))
        if opcion == 1:
            os.system("cls")
            nombre = (input("ingrese su nombre :3 \n"))
            while nombre == "" or nombre == " ":
                nombre =(input("\ningrese su fkin nombre! 7u7 \n"))
            direccion = int(input("ingrese su direccion!!!!\n"))
            while direccion == " " or direccion == "":
                direccion = (input("ingrese su fkin direccion bien!!!!! >:v \n"))
            
            try:
                reserva = True
                while reserva:
                    numero_reserva = int(input("ingrese su numero de reserva: (no puede ser menor a 1000 o mayor a 9999)")
                    if numero_reserva > 999 or numero_reserva < 10000:
                        print("Numero de reserva registrado con exito uwu ")
                        
                    else:
                        os.system("cls")
                        print("el numero de reserva no es valida!!!!!!!!!!! xfavor hace la wea bien")
            except:
                print("\nel numero de reserva no es validooooooooooooo, yapo mierdaaa ")
                
            try:
                edad = True
                while edad:
                    edad = int(input("ingrese su edad! (De 18 a 120 uwu)"))
                    if edad > 17 and edad > 121:
                        print("\n Edad registrada exitosamente!!!!")
                        edad = False
                    else:
                        os.system("cls")
                        print("La edad no es valida u.u xfa ingrese una valida!")
            except:
                print("La edad no es valida!!!!!!!!!!!!!!!!!! intenta con numeros enteros uwu ")
                
                        
            correo = (input("ingrese su correo electronico \n"))
            while '@' not in correo:
                correo = (input("su correo debe poseer almenos un @ :3 \n"))
            try:
                acompañante = True
                while acompañante:
                    acomp = int(input("ingrese el numero de acompañantes!"))
                    if acomp >= 0:
                        print("numero de acompañantes registrado con exito!!!! ")
                        acompañante = False
                    else:
                        os.system("cls")
                        print("el numero de acompañantes no es valido :((((")
            except:
                print("el numero de acompañantes no es valido ! :c ")
                
                
        elif opcion == 2:
            user = input("\ningrese usuario de admin: ")
            password = input("ingrese contraseña de admin ")
            if user == admin and password == passAdmin:
                os.system("cls")
                print("\nCredenciales confirmadas!!! ")
                of acomp > 3:
                    
                print("Datos del Huésped! :33 ")
                print("Su nombre: {nombre}")
                print("Su direccion es: {direccion}")
                print("Su numero de reserva uwu: {numero_reserva}")
                print("Su edad: {edad}")
                print("Su correo electronico!: {correo}")
                print("su total de acompañante: {acompañante}")
                print("**** Huesped con demasiados acompañantes")
                time.sleep(3)
            else:
                print("---------Datos de Huesped!---------")
                print(f"Nombre : {nombre}")
                print(f"direccion {direccion}")
                print(f"numero de reserva: {numero_reserva}")
                print(f"Edad: {edad}")
                print(f"Numero de acompañantes")
                
            
            
    except:
        print("opcion no valida")