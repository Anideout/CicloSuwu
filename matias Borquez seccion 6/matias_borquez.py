import os, time
os.system("cls")
nombre = ""
user_admin = "admin"
passw_admin = "1234"
bandMenu = True
while bandMenu:
    print("Bienvenido al exitoso juego Call of Honor!!!!! donde jugaras por tu honor o algo así ")
    print("-------Sistema de Gestion de Jugadores -  **Epic Quest** -------")
    print("1.registrar jugador! ")
    print("2. Consultar datos de jugador ")
    print("3. SALIR u.u")
    try:
        opc = int(input("\ningrese una opcion valida uwu  \n"))
        if opc == 1:
            os.system("cls")
            print("Registrar usuario! ")
            nombre = input("\ningrese su nombre por favor uwu, recuerde que no puede dejar el espacio en blanco \n")
            while nombre == "" or nombre == " ":
                nombre = input("\ningrese su nombre de nuevo por favor, ya que usted es experto en no obedecer xd \n")
            
            try:
                bandID = True
                while bandID:
                    id_jugador = int(input("\ningrese su id por favor uwu recuerde que tiene que ser entre 10000 y 100000\n"))
                    if id_jugador > 9999 and id_jugador < 100000:
                        print("id registrado con exito ! ")
                        bandID = False
                    else:
                        os.system("cls")
                        print("\nsu id no ha podido ser registrado u.u recuerde que tiene que ser mayor a 10000 y menor a 10000!!\n ")
                        
            except:
                print("id mal ingresado, recuerda que debe estar dentro del rango -.- ")
                
            try:
                banNivel = True
                while banNivel:
                    nivel = int(input("ingrese su nivel por favor uwu recuerde que debe estar entre 1 y 100 uwu \n"))
                    if nivel >= 1 and nivel <= 101:
                        print("su nivel ha sido registado con exito ")
                        banNivel = False
                        
                    else:
                        os.system("cls")
                        print("su nivel no se ha podido registrar u.u intente de nuevo por favor ")
            except:
                os.system("cls")
                print("su nivel no ha podido ser registrado u.u intente nuevameteeeeeeeeeeeeeeeeeeeeeeee y esta vez hazlo bnn ")                
            
            correo = input("\ningrese su correo electronico por favor uwu, recuerde que debe contener un @ para que sea valido ! \n")
            while '@' not in correo:
                correo = input("\ningresa el correo bien we :v te estoy diciendo que debe contener un @ para que sea valido \n")
                
            try:
                bandRol = True
                while bandRol:
                    rol_jugador = input("\ningrese su rol en el juego!: Objetive uwu, Slayer >:), Support unu, anchor :3 \n")
                    if rol_jugador == "Objective" or rol_jugador == "objective" or rol_jugador == "Slayer" or rol_jugador == "slayer" or  rol_jugador == "Support" or rol_jugador == "support" or rol_jugador == "Anchor" or rol_jugador == "anchor":
                        bandRol = False
                        print("rol ingresado con exito uwu ")
                    else:
                        print("\nsu rol no ha podido ser registrado, ya que lo ingresaste mal we xd te toi diciendo y ni así \n")
                
                    
                             
            except:
                os.system("cls")
                print("\noye yapo ingresalo bien :c\n ")
            try:
                bandExp = True
                while bandExp:
                    experiencia = int(input("\ningrese su total de puntos de experiencias!! uwu\n"))
                    if experiencia >= 0 or experiencia == "" or experiencia == " ":
                        print("experiencia registrada con exito ! uwu ")
                        bandExp = False
                        time.sleep(2)
                        os.sytem("cls")
                    else:
                        print("\nnumero de experiencia no valido u.u intente con numeros enteros esta vez uwu \n")
                        
            except:
                print("su numero de experiencia no es valido u.u como vas a tener -0 we que onda lo manco ")
               
                os.system("cls")
            
            
        elif opc == 2:
            os.system("cls")
            print("consultar datos de jugador! ")
            usuario = input("\ningrese su nombre de usuario! \n")
            password = input("\ningrese su contraseña por favor \n")
            if usuario == user_admin and password == passw_admin:
                print("bienvenido don administrador uwu ")
                os.system("cls")
                try:
                    bandID2 = True
                    while bandID2:
                        id_usuario2 = int(input("\ningrese el id del jugador uwu \n"))
                        if id_usuario2 == id_jugador :
                            print("id encontrado :3 " )
                            bandID2 = False
                            if nivel > 50 and experiencia > 1000:
                                print("----------datos del jugado! ---------")
                                print(f"Nombre: don {nombre}")
                                print(f"Id: {id_jugador}")
                                print(f"Nivel del jugador: {nivel}")
                                print(f"Rol del jugador: {rol_jugador}")
                                print(f"Puntos de experiencias: {experiencia}")
                                print(f"Este es un jugador experimentado! terrible pro oiga ")
                                time.sleep(4)
                                os.system("cls")
                                
                            elif nivel < 50 and experiencia < 1000:
                                print("----------datos del jugado! ---------")
                                print(f"Nombre: don {nombre}!")
                                print(f"Id: {id_jugador}!")
                                print(f"Nivel del Jugador: {nivel}!")
                                print(f"Rol del Jugador: {rol_jugador}!")
                                print(f"Puntos de Experiencias: {experiencia}!")
                                print(f"Este jugado es novato, terrible noob oiga ")
                                time.sleep(4)
                                os.system("cls")
                        else:
                            print("id no encontrado :c ")
                            
                except:
                    os.system("cls")
                    print("id no coincide con ningun jugador u.u intente de nuevo ! ")
                
                
                    
   
        elif opc == 3:
            os.system("cls")
            print("usted ha salido del sistema  u/////u f")
            
        
        
        
    
            
    except:
        os.system("cls")
        print("opcion no valida")
            