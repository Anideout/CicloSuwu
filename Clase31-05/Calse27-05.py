"""

⮚	Rut, sin dígito verificador ni puntos. X

⮚	Nombre X

⮚	Dirección X

⮚	Correo X

⮚	Edad (número entero entre 0 y 110) X

⮚	Sexo, solo puede aceptar como caracteres las letras f o m X

⮚	Registros

⮚	PS, acepta sólo que se ingrese Isapre o Fonasa (no es necesario especificar la Isapre) X

"""


import os,time


os.system("cls")

banMen1 = True


registrosP = []


while banMen1:
    
    printt("\n**********************")
    printt("---------Menu---------")
    printt("1) Registrar Paciente")
    printt("2) Atención Paciente")
    printt("3) Gestionar Paciente")
    printt("4) Salir")

    try:

        opc1 = int(input("\nIngrese su opción: "))
        

        if opc1 == 1:

            banPaciente = True

            while banPaciente:

                # Rut del paciente

                banRut = True

                while banRut:

                    try:

                        rut = int(input("\nIngrese su rut (Sin dígito verificador ni puntos): "))

                        if rut >= 5000000 and rut <= 99999999:

                            os.system("cls")
                            printt("\nRut registrado.")

                            banRut = False

                            time.sleep(1)

                        else:

                            os.system("cls")
                            printt("\nRut no válido. Intente con un rango de 5000000 a 99999999.")

                    except:

                        os.system("cls")
                        printt("\nUsted a ingresado un rut no válido. Intente con números enteros positivos.")
                

                # Nombre del paciente

                os.system("cls")

                banNombre = True

                while banNombre:

                    nombre = input("\nIngrese su nombre: ")

                    if nombre != "":

                        os.system("cls")
                        printt("\nNombre registrado.")

                        banNombre = False

                        time.sleep(1)

                    else:

                        os.system("cls")
                        printt("\nNombre vacío. Intente nuevamente.")
                

                # Dirección del paciente

                os.system("cls")

                banDir = True

                while banDir:

                    direccion = input("\nIngrese su dirección: ")

                    if nombre != "":

                        os.system("cls")
                        printt("\nDirección registrado.")

                        banDir = False

                        time.sleep(1)

                    else:

                        os.system("cls")
                        printt("\nDirección vacía. Intente nuevamente.")
                        

                # Correo paciente

                os.system("cls")

                banCorreo = True

                while banCorreo:

                    correo = input("\nIngrese su correo (Debe de tener un @): ")

                    if "@" in correo:

                        os.system("cls")
                        printt("\nCorreo registrado.")

                        banCorreo = False

                        time.sleep(1)

                    else:

                        os.system("cls")
                        printt("\nCorreo no válido. Intente nuevamente agregando un @")
                

                # Edad paciente

                os.system("cls")

                banEdad = True

                while banEdad:

                    try:

                        edad = int(input("\nIngrese su edad (Debe de estar entre 0 a 110 años): "))

                        if edad >= 0 and edad <= 110:

                            os.system("cls")
                            printt("\nEdad registrada.")

                            banEdad = False

                            time.sleep(1)

                        else:

                            os.system("cls")
                            printt("\nEdad no válida. Intente con una edad entre el rango de 0 a 110 años.")

                    except:

                        os.system("cls")
                        printt("\nEdad no válida. Intente con números enteros positivos.")
                        

                # Sexo paciente

                os.system("cls")

                banSexo = True

                while banSexo:

                    sexo = input("\nIngrese el sexo (Femenino = 'f', Masculino = 'm'): ")

                    if sexo.upper() == "F" or sexo.upper() == "M":

                        os.system("cls")
                        printt("\nSexo registrado.")

                        banSexo = False

                        time.sleep(1)

                    else:

                        os.system("cls")
                        printt("\nSexo no válido. Intente con las iniciales de Femenino o Masculino.")
                

                # PS

                os.system("cls")

                banPs = True

                while banPs:

                    ps = input("\nIngrese su PS (ISAPRE o FONASA): ")

                    if ps == "ISAPRE" or ps == "FONASA":

                        os.system("cls")
                        printt("\nPS registrado.")

                        banPs = False

                        time.sleep(1)

                    else:

                        os.system("cls")
                        printt("\nPS no válido. Intente agregando Fonasa o Isapre en mayusculas.")
                

                registro = "No disponible"
                

                paciente = {

                    "Rut" : rut,

                    "Nombre" : nombre,

                    "Direccion" : direccion,

                    "Correo" : correo,

                    "Edad" : edad,

                    "Sexo" : sexo,

                    "PS" : ps,

                    "Registro" : registro

                }
                

                registrosP.append(paciente)
                

                os.system("cls")

                banOtrop = True

                while banOtrop:

                    try:
                        printt("\n¿Desea agregar otro paciente?")
                        printt("1) Si")
                        printt("2) No")

                        opc2 = int(input("\nIngrese su opción (1 o 2): "))

                        if opc2 == 1:

                            os.system("cls")
                            printt("\nPreparando nuevo registro...")

                            time.sleep(1)

                            banOtrop = False

                        elif opc2 == 2:

                            os.system("cls")
                            printt("\nCerrando registro...")

                            banPaciente = False

                            time.sleep(1)

                            banOtrop = False

                        else:

                            os.system("cls")
                            printt("\nOpción no válida. Intente con el número entero 1 o 2.")

                    except:

                        os.system("cls")
                        printt("\nOpción no válida. Intente con un número entero positivo.")
                    

        elif opc1 == 2:

            os.system("cls")
            printt("\n¿Que paciente desea atender?")

            try:

                rut_pac = int(input("\nIngrese el rut del paciente: "))
                

                for paciente in registrosP:

                    if paciente["Rut"] == rut_pac:

                        os.system("cls")

                        fecha = input("\nIngrese la fecha de la visita: ")

                        while fecha == "":

                            os.system("cls")

                            fecha = input("\nIngrese la fecha de la visita (No puede estar vacio): ")
                        

                        os.system("cls")

                        observacion = input("\nIngrese las observaciones del paciente en la visita:\n")

                        while observacion == "":

                            os.system("cls")

                            observacion = input("\nIngrese las observaciones del paciente en la visita (No puede estar vacio):\n")
                        

                        rec_registro = f"Fecha de la visita: {fecha}\nObservaciones: {observacion}"

                        paciente["Registro"] = rec_registro
                        

                        os.system("cls")
                        printt("Registro del paciente guardado con éxito.")

                        break

                    else:

                        os.system("cls")
                        printt("\nBuscando paciente...")

                        time.sleep(1)

            except:
                printt("\nOpción no válida. Intente con un número entero positivo.")
        

        elif opc1 == 3:

            os.system("cls")

            banMen2 = True

            while banMen2:
                printt("\n********************************")
                printt("------Menu de modificación------")
                printt("1) Consultar datos del paciente")
                printt("2) Eliminar un paciente")
                printt("3) Modificar datos del paciente")
                printt("4) Regresar al menu principal")

                try:

                    opc3 = int(input("Ingrese la opción que desea: "))

                    if opc3 == 1:

                        os.system("cls")

                        try:

                            rut_pac = int(input("\nIngrese el rut del paciente: "))

                            for paciente in registrosP:

                                if paciente["Rut"] == rut_pac:

                                    os.system("cls")
                                    printt(f"Rut: {paciente["Rut"]}")
                                    printt(f"Nombre: {paciente["Nombre"]}")
                                    printt(f"Dirección: {paciente["Direccion"]}")
                                    printt(f"Correo: {paciente["Correo"]}")
                                    printt(f"Edad: {paciente["Edad"]}")
                                    printt(f"Sexo: {paciente["Sexo"]}")
                                    printt(f"PS: {paciente["PS"]}")
                                    printt(f"Registro: \n{paciente["Registro"]}")

                                    time.sleep(3)

                                    break

                                else:

                                    os.system("cls")
                                    printt("\nBuscando paciente...")

                                    time.sleep(1)

                        except:

                            os.system("cls")
                            printt("\nOpción de rut no válida. Intente con un número entero positivo.")
                            

                    elif opc3 == 2:

                        os.system("cls")

                        try:

                            rut_pac = int(input("\nIngrese el rut del paciente: "))

                            for paciente in registrosP:

                                if paciente["Rut"] == rut_pac:

                                    os.system("cls")

                                    registrosP.remove(paciente)
                                    printt("\nPaciente eliminado.")

                                    time.sleep(2)

                                    break

                                else:

                                    os.system("cls")
                                    printt("\nBuscando paciente...")

                                    time.sleep(1)

                        except:

                            os.system("cls")
                            printt("\nOpción de rut no válida. Intente con un número entero positivo.")
                            

                    elif opc3 == 3:

                        os.system("cls")

                        try:

                            rut_pac = int(input("\nIngrese el rut del paciente: "))

                            for paciente in registrosP:

                                if paciente["Rut"] == rut_pac:

                                    os.system("cls")

                                    banMen3 = True

                                    while banMen3:

                                        # En proceso...
                                        printt("\n¿Que datos desea modificar?")
                                        printt("Rut")
                                        printt("Nombre")
                                        printt("Dirección")
                                        printt("Correo")
                                        printt("Edad")
                                        printt("Sexo")
                                        printt("PS")

                                        opc4 = input("Ingrese su Campo a editar: ")

                                        for x in paciente:
                                            printt(f"¿Desea editar el campo {paciente[x]}?")

                                            opc4 = int(input("1) Si     2) No   : "))
                                    

                                    break

                                else:

                                    os.system("cls")
                                    printt("\nBuscando paciente...")

                                    time.sleep(1)

                        except:
                            printt("\nOpción de rut no válida. Intente con un número entero positivo.")

                except:
                    printt("Opción de menú no válida. Intente con números enteros positivos.")

        elif opc1 == 4:

            os.system("cls")

            banMen1 = False
            printt("\nSaliendo del sistema...")

            time.sleep(1)

            os.system("cls")
            printt("\n¡Hasta luego!")
            

    except:
        printt("\nUsted ha ingresado una opción erronea. Intente con números enteros positivos (1-4).")