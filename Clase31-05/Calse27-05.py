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
    
    print("\n**********************")
    print("---------Menu---------")
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Gestionar Paciente")
    print("4) Salir")
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
                            print("\nRut registrado.")
                            banRut = False
                            time.sleep(1)
                        else:
                            os.system("cls")
                            print("\nRut no válido. Intente con un rango de 5000000 a 99999999.")
                    except:
                        os.system("cls")
                        print("\nUsted a ingresado un rut no válido. Intente con números enteros positivos.")
                
                # Nombre del paciente
                os.system("cls")
                banNombre = True
                while banNombre:
                    nombre = input("\nIngrese su nombre: ")
                    if nombre != "":
                        os.system("cls")
                        print("\nNombre registrado.")
                        banNombre = False
                        time.sleep(1)
                    else:
                        os.system("cls")
                        print("\nNombre vacío. Intente nuevamente.")
                
                # Dirección del paciente
                os.system("cls")
                banDir = True
                while banDir:
                    direccion = input("\nIngrese su dirección: ")
                    if nombre != "":
                        os.system("cls")
                        print("\nDirección registrado.")
                        banDir = False
                        time.sleep(1)
                    else:
                        os.system("cls")
                        print("\nDirección vacía. Intente nuevamente.")
                        
                # Correo paciente
                os.system("cls")
                banCorreo = True
                while banCorreo:
                    correo = input("\nIngrese su correo (Debe de tener un @): ")
                    if "@" in correo:
                        os.system("cls")
                        print("\nCorreo registrado.")
                        banCorreo = False
                        time.sleep(1)
                    else:
                        os.system("cls")
                        print("\nCorreo no válido. Intente nuevamente agregando un @")
                
                # Edad paciente
                os.system("cls")
                banEdad = True
                while banEdad:
                    try:
                        edad = int(input("\nIngrese su edad (Debe de estar entre 0 a 110 años): "))
                        if edad >= 0 and edad <= 110:
                            os.system("cls")
                            print("\nEdad registrada.")
                            banEdad = False
                            time.sleep(1)
                        else:
                            os.system("cls")
                            print("\nEdad no válida. Intente con una edad entre el rango de 0 a 110 años.")
                    except:
                        os.system("cls")
                        print("\nEdad no válida. Intente con números enteros positivos.")
                        
                # Sexo paciente
                os.system("cls")
                banSexo = True
                while banSexo:
                    sexo = input("\nIngrese el sexo (Femenino = 'f', Masculino = 'm'): ")
                    if sexo.upper() == "F" or sexo.upper() == "M":
                        os.system("cls")
                        print("\nSexo registrado.")
                        banSexo = False
                        time.sleep(1)
                    else:
                        os.system("cls")
                        print("\nSexo no válido. Intente con las iniciales de Femenino o Masculino.")
                
                # PS
                os.system("cls")
                banPs = True
                while banPs:
                    ps = input("\nIngrese su PS (ISAPRE o FONASA): ")
                    if ps == "ISAPRE" or ps == "FONASA":
                        os.system("cls")
                        print("\nPS registrado.")
                        banPs = False
                        time.sleep(1)
                    else:
                        os.system("cls")
                        print("\nPS no válido. Intente agregando Fonasa o Isapre en mayusculas.")
                
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
                        print("\n¿Desea agregar otro paciente?")
                        print("1) Si")
                        print("2) No")
                        opc2 = int(input("\nIngrese su opción (1 o 2): "))
                        if opc2 == 1:
                            os.system("cls")
                            print("\nPreparando nuevo registro...")
                            time.sleep(1)
                            banOtrop = False
                        elif opc2 == 2:
                            os.system("cls")
                            print("\nCerrando registro...")
                            banPaciente = False
                            time.sleep(1)
                            banOtrop = False
                        else:
                            os.system("cls")
                            print("\nOpción no válida. Intente con el número entero 1 o 2.")
                    except:
                        os.system("cls")
                        print("\nOpción no válida. Intente con un número entero positivo.")
                    
        elif opc1 == 2:
            os.system("cls")
            print("\n¿Que paciente desea atender?")
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
                        print("Registro del paciente guardado con éxito.")
                        break
                    else:
                        os.system("cls")
                        print("\nBuscando paciente...")
                        time.sleep(1)
            except:
                print("\nOpción no válida. Intente con un número entero positivo.")
        
        elif opc1 == 3:
            os.system("cls")
            banMen2 = True
            while banMen2:
                print("\n********************************")
                print("------Menu de modificación------")
                print("1) Consultar datos del paciente")
                print("2) Eliminar un paciente")
                print("3) Modificar datos del paciente")
                print("4) Regresar al menu principal")
                try:
                    opc3 = int(input("Ingrese la opción que desea: "))
                    if opc3 == 1:
                        os.system("cls")
                        try:
                            rut_pac = int(input("\nIngrese el rut del paciente: "))
                            for paciente in registrosP:
                                if paciente["Rut"] == rut_pac:
                                    os.system("cls")
                                    print(f"\nRut: {paciente["Rut"]}")
                                    print(f"Nombre: {paciente["Nombre"]}")
                                    print(f"Dirección: {paciente["Direccion"]}")
                                    print(f"Correo: {paciente["Correo"]}")
                                    print(f"Edad: {paciente["Edad"]}")
                                    print(f"Sexo: {paciente["Sexo"]}")
                                    print(f"PS: {paciente["PS"]}")
                                    print(f"Registro: \n{paciente["Registro"]}")
                                    time.sleep(3)
                                    break
                                else:
                                    os.system("cls")
                                    print("\nBuscando paciente...")
                                    time.sleep(1)
                        except:
                            os.system("cls")
                            print("\nOpción de rut no válida. Intente con un número entero positivo.")
                            
                    elif opc3 == 2:
                        os.system("cls")
                        try:
                            rut_pac = int(input("\nIngrese el rut del paciente: "))
                            for paciente in registrosP:
                                if paciente["Rut"] == rut_pac:
                                    os.system("cls")
                                    registrosP.remove(paciente)
                                    print("\nPaciente eliminado.")
                                    time.sleep(2)
                                    break
                                else:
                                    os.system("cls")
                                    print("\nBuscando paciente...")
                                    time.sleep(1)
                        except:
                            os.system("cls")
                            print("\nOpción de rut no válida. Intente con un número entero positivo.")
                            
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
                                        print("\n¿Que datos desea modificar?")
                                        print("Rut")
                                        print("Nombre")
                                        print("Dirección")
                                        print("Correo")
                                        print("Edad")
                                        print("Sexo")
                                        print("PS")
                                        opc4 = input("Ingrese su Campo a editar: ")
                                        for x in paciente:
                                            print(f"¿Desea editar el campo {paciente[x]}?")
                                            opc4 = int(input("1) Si     2) No   : "))
                                    
                                    break
                                else:
                                    os.system("cls")
                                    print("\nBuscando paciente...")
                                    time.sleep(1)
                        except:
                            print("\nOpción de rut no válida. Intente con un número entero positivo.")
                except:
                    print("Opción de menú no válida. Intente con números enteros positivos.")
        elif opc1 == 4:
            os.system("cls")
            banMen1 = False
            print("\nSaliendo del sistema...")
            time.sleep(1)
            os.system("cls")
            print("\n¡Hasta luego!")
            
    except:
        print("\nUsted ha ingresado una opción erronea. Intente con números enteros positivos (1-4).")