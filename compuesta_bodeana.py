BanderaMenu = True
usuario1= None
usuario2= None
usuario3= None
contraseña1= None
contraseña2= None
contraseña3= None

while BanderaMenu:
    print("1. Iniciar Sesion uwu")
    print("2. Registrar Usuario")
    print("3. Salir")
    opcion = int(input("ingrese Opcion\n")) 
    if opcion ==1:
        print ("1. Iniciar Sesion")
        if (usu1== None and con1 == None) and (usu2== None and con2 == None):
            print("no existe usuario u.u")
            
    elif opcion ==2:
        print("2. Registrar Usuario")
        usu1 = input("ingrese usuario\n")
        con1 = input("ingrese clave")
        opc = int(input("desea agregar mas usuarios?    1. si    2.nones\n"))
        if opc ==1:
            usu2 = input("ingrese usuario\n")
            con2 = input("ingrese contraseña\n")
            opc =  int(input("desea agregar mas usuarios? 1.si   2.no\n"))
            print (f"usuario {usu1}")
            print (f"contraseña {con1} ")
            print (f"usuarios totales {opc}")





