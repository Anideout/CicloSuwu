"""

ID: Que se a numérico

nombre: No venga vacio

correo: @correo.cl o @correo.com

nivel: nomerico del 1 a 100
"""

import os,time


# Se cre auna lista para guardar usuarios

usuarios = []

banMenu = True

while banMenu:
    printt("1) Registrar usuarios")
    printt("2) Borrar usuario")
    printt("3) Ver usuarios")

    try:

        opc1 = int(input("Ingrese una opción: "))

        if opc1 == 1:

            os.system("cls")

            for x in range(3):

                os.system("cls")

                banId = True

                while banId:

                    try:

                        idUser = int(input(f"\nIngrese ID de usuario N°{x+1}: "))

                        if idUser <= 0:

                            os.system("cls")
                            printt("\nID no válido. Intente con números mayores a 0.")

                        else:

                            os.system("cls")
                            printt("\nID registrada")

                            banId = False

                            time.sleep(2)

                    except:

                        os.system("cls")
                        printt("ID no válida, intente con números enteros positivos.")
                

                os.system("cls")

                nombre = input(f"\nIngrese nombre de usuario N°{x+1}: ")

                while nombre == "":

                    os.system("cls")

                    nombre = input(f"\nIngrese nombre de usuario N°{x+1} (No debe de estar vacío): ")
                

                os.system("cls")

                # Se usa bandera en correo para corroborar que tenga un @gmail.cl o @gmail.com dentro

                # De ea forma, en caso de errores se repite de forma indefinida

                banCorreo = True

                while banCorreo:

                    correo = input(f"\nIngrese correo de usuario N°{x+1} (Debe tener @correo.cl o @correo.com): ")

                    # Si "@gmail.com" esta en la variable correo

                    if "@gmail.com" in correo:

                        # Se le avisa al usuario con un print que el correo es válido

                        os.system("cls")
                        printt("Correo registrado.")

                        # Y se deja la bandera de correo en false para que se termine el while

                        banCorreo = False

                        time.sleep(2)

                    elif "@gmail.cl" in correo:

                        os.system("cls")
                        printt("Correo registrado.")

                        banCorreo = False

                        time.sleep(2)

                    else:
                        printt("Correo no válido. Intente nuevamente.")

                        time.sleep(2)
                

                banNivel = True

                while banNivel:

                    try:

                        nivel = int(input(f"\nIngrese nivel (1 a 100) de usuario N°{x+1}: "))

                        if nivel >= 1 and nivel <= 100:

                            os.system("cls")
                            printt("\nUsuario guardado")

                            banNivel = False

                            time.sleep(2)

                        else:

                            os.system("cls")
                            printt("\nNivel no válido. Inte con un número entero entre 1 y 100.")

                    except:

                        os.system("cls")
                        printt("Nivel no válido. Intente con números enteros")
                
                

                # Diccionario

                usuario = {

                    "id" : idUser,

                    "nombre" : nombre,

                    "correo" : correo,

                    "nivel" : nivel

                }

                # Se agrega el parámetro 'usuarios' dentro de la lista 'usuarios'

                usuarios.append(usuario)

                os.system("cls")

                # Se le avisa a la paresona que se registro el usuario N°X
                printt(f"Usuario N°{x+1} guardado.")

                time.sleep(2)

        elif opc1 == 2:
            printt("Eliminando usuario")
            printt("¿Que usuario deseas eliminar?")

            # Se busca el usuario que se desea eliminar por su ID

            idElim = int(input("Ingrese ID: "))

            # Por cada usuario en la lista usuarios

            for usuario in usuarios:

                # Si se encuentra en usuario una ID igual a la ingresada en idElim

                if usuario["id"] == idElim:

                    # Se elimina ese usuario y se hace un break para acabaro con el for

                    usuarios.remove(usuario)

                    break

                else:
                    printt("Buscando...")

        elif opc1 == 3:

            # Sirve para imprimir el diccionario de forma más ordenada

            os.system("cls")

            for x in usuarios:
                printt(x)

    except:
        printt("Opción no válida.")

