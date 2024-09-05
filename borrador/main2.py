import time, os
banderaMenu = True
usu1= None 
usu2=None 
usu3=None
con1= None 
con2=None 
con3= None

while banderaMenu:
    print("1. Iniciar Sesion")
    print("2. Registrar Usuario")
    print("3. Salir")
    try:
        opcion = int(input("ingrese opcion\n"))
        if opcion ==1 :
            os.system("cls")
            print("1. Iniciar Sesion")
            if (usu1 is None and con1 is None) and (usu2 is None and con2 is None)and (usu3 is None and con3 is None):
                print("No existen usuarios para acceder.")
                time.sleep(2)
                continue

            else:
                username = input("Ingrese su nombre de usuario: \n")
                password = input("Ingrese su contraseña: \n")
                if (username == usu1 and password == con1) or (username == usu2 and password == con2) or (username == usu3 and password == con3):
                    os.system("cls")
                    while True:
                        print("1. Realizar llamada")
                        print("2. Enviar correo electrónico")
                        print("3. Salir")
                        try:
                            opcion2 = int(input("Ingrese opción: \n"))
                            if opcion2 == 1:
                                os.system("cls")
                                print("1. Realizar llamada")
                                numero = input("Por favor, ingresa el número de celular (debe comenzar con 9 y tener 9 dígitos): \n")
                                if len(numero) == 9 and numero.startswith('9'):
                                    print("Llamando al número", numero)
                                    time.sleep(2)
                                    
                                else:
                                    print("El número ingresado no es válido. Debe comenzar con 9 y tener 9 dígitos.\n")
                                    time.sleep(2)
                                    
                            elif opcion2 ==2:
                                
                                os.system("cls")
                                print("2. Enviar correo electrónico")
                                correo = input("Por favor, ingresa tu correo electrónico: \n")
                                while '@' not in correo:
                                    print("El correo electrónico debe contener '@'.")
                                    correo = input("Por favor, ingresa tu correo electrónico: \n")
                                print("Correo electrónico guardado:", correo)
                                time.sleep(2)
                                os.system("cls")
                                mensaje = input("ingrese mensaje\n")
                                print(f"DE: {username}")
                                print(f"PARA: {correo}")
                                print(f"MENSAJE: {mensaje}")
                                break
                            else:
                                os.system("cls")
                                print("3. Salir")
                                break
                        except:
                            print("opcion ingresa no existe :@")
        elif opcion == 2:
            os.system("cls")
            print("2. Registrar Usuario")
            usu1 = input("ingrese usuario\n")
            con1 = input("ingrese clave\n")
            opc = int(input("desea agregar mas usuarios?  1.si  2.no\n"))
            if opc == 1:
                usu2 = input("ingrese usuario\n")
                con2 = input("ingrese clave")
                opc = int(input("desea agregar mas usuarios?  1.si  2.no\n"))
                if opc == 1:
                    usu3 = input("ingrese usuario\n")
                    con3 = input("ingrese clave")
                    print(f"usuario: {usu1}")
                    print(f"clave: ******")
                    print(f"usuario: {usu2}")
                    print(f"clave: ******")
                    print(f"usuario: {usu3}")
                    print(f"clave: ******")
                else:
                    print(f"usuario: {usu1}")
                    print(f"clave: ******")
                    print(f"usuario: {usu2}")
                    print(f"clave: ******")
            else:
                print(f"usuario: {usu1}")
                print(f"clave: ******")
        elif opcion == 3:
            os.system("cls")
            print("3. Salir")
            banderaMenu = False
        else:
            print("opcion  no valida")
    except:
        print("opcion ingresada no exisate")
print("shao, loh vimoh")        
        
       
