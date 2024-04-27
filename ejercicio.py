import time, os
BanderaMenu = True
usu1= None
usu2= None
usu3= None
con1= None
con2= None
con3= None
telefono = None
Email= None

while BanderaMenu:
    print("1. Iniciar Sesion uwu")
    print("2. Registrar Usuario")
    print("3. Salir")
    opcion = int(input("ingrese Opcion\n")) 
    if opcion ==1:
        print ("1. Iniciar Sesion")
        if (usu1 is None and con1 is None) and (usu2 is None and con2 is None) and (usu3 is None and con3 is None):
            print("no existe usuario u.u")
            time.sleep(2)
            continue
        else:
            username = input("ingrese su nombre de usuario: \n")
            password = input("ingrese su contraseña: \n")
            if(username == usu1 and password == con1) or (username == usu2 and password == con2) or (username == usu3 and password == con3):
            os.system("cls")
            print("1. Realizar llamada")
            print("2. registrar correo ")
            print("3. salir")
            opcion2 = int(input("ingrese opcion\n"))
            if opcion == 1:
                while True:
                    os.system("cls")
                    print("realizar llamada")
                    numero = input("Ingresa el numero we (recuerda que debe comenzar del 9 y tener 9 digitos >.<)")
                    if len(numero) == 9 and numero.startswitch(9)
                        print("llamando al numero uwu ", numero)
                        time.sleep(2)
                        
                    else:
                        print("su opcion no es valida :((( recuerda que tu numero debe empezar con 9 y tener 9 digitos !!!!!!!!!!!!!!")
                        time.sleep(2)
            elif opcion2 ==2:
                os.system("cls")
                print("2. enviar correo electronico")
                correo = input("por favor ingresa el correo ;C\n")
                
            
    elif opcion ==2:
        print("2. Registrar Usuario")
        usu1 = input("ingrese usuario\n")
        con1 = input("ingrese contraseña\n")
        opc = int(input("desea agregar mas usuarios?    1. si    2.nones\n"))
        if opc ==1:
            usu2 = input("ingrese usuario\n")
            con2 = input("ingrese contraseña\n")
            opc =  int(input("desea agregar mas usuarios? 1.si   2.no\n"))
            if opc == 1:
                usu3 = input("ingrese usuario\n")
                con3 = input("ingrese contraseña\n")
                print (f"usuario:  {usu1}")
                print (f"contraseña *******")
                print (f"usuario:  {usu2}")
                print (f"contraseña *******")
                print (f"usuario: {usu3}")
                print (f"contraseña *******")
            else:
                print(f"usuario: {usu1}")
                print(f"contraseña *******")
                print(f"usuario: {usu2}")
                print(f"contraseña: ******")
        else:
            print (f"usuario: {usu1}")
            print(f"contraseña: ******")
    elif opcion == 3:
        print("usted ha salido uwu vuelva pronto!")
        BanderaMenu= False
    else:
        print("opcion no valida mierda!!!!!!!!!!!!!!!!!!!!!!!!!!! intenta de nuevo >:(")
        

    
    

            
            
    