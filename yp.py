import os, time 
bandMenu = True
os.system("Cls")

while bandMenu:
    print("\t\t Bienvenido al selector de usuarios gays uwu  ")
    print("1. Inicio de sesion ")
    print("2. Eliminar usuario")
    print("3. Salir ")
    try:
        opc = int(input("ingrese una opcion uwu \n"))
        if opc == 1:
            print("\tInicio de sesion!!!!!!!\t")
            usuario = input("ingrese su nombre de usuario  \n")
            contraseña = input("ingrese su contraseña uwu ")
            
    except:
        print("opcion no valida :c ")