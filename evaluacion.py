import os, time

os.system("clear")
MENU = True
while MENU:
    print("1. Registrar usuario")
    print("2. Eliminar usuario ! ")
    print("3. Salir")
    try:
        
        opc = int(input("\tingrese su opcion! \n"))
        if opc == 1:
            os.system("clear")
            usuarios = []
            for x in range(3):
                idUsuario = int(input("\tIngrese el id de jugador por favor \n"))
                nombre = input("\tIngrese nombre de usuario \n")
                while nombre == "" or nombre == " ":
                    nombre = input("\t Ingrese su nombre por favor \n")
                correo = input("\tIngrese correo \n")
                while '@'not in correo and "gmail.com" not in correo and "gmail.cl":
                    correo = input("\t Ingrese su correo electronico por favor \n")
                bandNivel = True
                while bandNivel:
                        try:
                            os.system("clear")
                            nivel = int(input("\tIngrese su nivel (desde 1 a 100 ) \n"))
                            if nivel >= 1 and nivel <= 100:
                                nivel = int(input("\tIngrese su nivel de usuario ! (desde 1 a 100) \n"))
                                bandNivel = False
                                os.system("clear")
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
        elif opc == 2:
            print("Eliminar usuario")
            rut_eliminar = int(input("Ingrese el rut del paciente por favor! \n"))
            for paciente in pacientes:
                for usuario in usuarios:
                    if usuario ["id"] == idMinimo:
                        usuarios.remove(usuario)

                    else:
                        for y in usuarios:
                            print(usuario)
                

    except:
        print("opcion no valida! ")

                        