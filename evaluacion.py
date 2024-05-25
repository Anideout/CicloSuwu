import os, time

os.system("cls")
usuarios = []
band = True
while band:
    print("\t1. Registrar usuario")
    print("\t2. Eliminar usuario ! ")
try:
    opc = int(input("\tingrese su opcion! \n"))
    if opc == 1:
        for x in range(3):
            idUsuario = int(input("\tIngrese el id de jugador por favor \n"))
            nombre = input("\tIngrese nombre de usuario \n")
            while nombre == "" or nombre == " ":
                nombre = input("\t Ingrese su nombre por favor \n")
            correo = input("\tIngrese correo \n")
            while '@'not in correo and "gmail.com" not in correo and "gmail.cl":
                correo = input("\t Ingrese su correo electronico por favor \n")
            try:
                os.system("cls")
                bandNivel = True
                while bandNivel:
                    nivel = int(input("\tIngrese su nivel (desde 1 a 100 ) \n"))
                    if nivel >= 1 and nivel <= 100:
                        nivel = int(input("\tIngrese su nivel de usuario ! (desde 1 a 100) \n"))
                        bandNivel = False
                        os.system("cls")
                    else:
                        print("nivel ingresado no valido u.u intente de nuevo! ")
                        
            except:
                print("nivel ingresado no valido, intente de nuevo ")
                
            #diccionario
            usuario = {
                "id" : idUsuario,
                "nombre" : nombre,
                "correo" : correo,
                "nivel " : nivel
            }
            usuarios.append(usuario)
            
        #id minimo
        idMinimo = min(usuario["id"] for usuario in usuarios)

        for usuario in usuarios:
            if usuario ["id"] == idMinimo:
                usuarios.remove(usuario)
            
        for y in usuarios:
            print(usuario)
            
    if opc == 2:
        print("Eliminar usuario")
    
    
except:
    print("opcion no valida ")