import os, time
pacientes = []
banMenu = True
os.system("clear")
while banMenu:
    print("\t1. Registrar paciente ! ")
    print("\t2. Atencion paciente! ")
    print("\t3. Gestionar paciente! ")
    print("\t4. Salir..")
    try:

        opc = int(input("ingrese opcion por favor \n"))
        if opc == 1:
            os.system("clear")
            bandPaciente = True
            while bandPaciente:
                bandRUT = True
                bandEdad = True
                print("\tRegistrar paciente! ")
                while bandRUT:
                    try:
                        rut= int(input("Ingrese rut! \n"))
                        if rut >= 5000000 and rut <= 99999999:
                            print("ta weno uwu ")

                            bandRUT = False

                        else:
                            print("ta  malo we ")

                    except:
                        os.system("clear")
                        print("no se permite ingresar caracteres en el rut! ")

                nombre = input("ingrese su nombre por favor \n")
                while nombre == "":
                    nombre = input("ingrese bn su puto nombre \n")
                direccion = input("ingrese su direccion por favor ! \n")
                while direccion == "":
                    direccion = input("ingrese bien su direccion por favor ! \n")
                correo = input("ingrese su correo porfavor uwu recuerde que debe contener un @ para que sea valido !\n")
                while '@' not in correo:
                    correo = input("ingrese bien su correo por favor \n")
                while bandEdad:
                    try:
                        edad = int(input("ingrese su edad por favor !\n"))
                        if edad > 0 and edad <= 110:
                            print("ta weno uwu ")
                            bandEdad = False
                        else:
                            print("ta malito ")
                    except:
                        print("invalido ! ")
                bandSexo = True
                while bandSexo:
                    try:

                        sexo = input("igrese su preferencia sexual por favor !indiquelo con un m o una f! \n")
                        while sexo.upper() == 'F' and sexo.upper() == 'M':
                            sexo = input("ingrese sexo por favor! solo existe masculino y femina no insista\n")
                    except:
                        print("")
                banPRE = True
                while banPRE:
                    prevision = input("ingrese prevision de salud \n")
                    if prevision.upper() == 'FONASA' or prevision.upper() == 'ISAPRE':
                        print("ta weno uwu ")
                        banPRE = False

                    else:
                        print("ingrese prevision de salud, solo acepta isapre o fonasa")
                paciente = [rut, nombre, direccion, correo, edad, sexo, prevision, registro]
                pacientes.append(paciente)
                agregarPaciente = input("Deseas agregar otro paciente ???? indique con 's' o 'n' \n")
                if agregarPaciente == 's':
                    continue
                else:
                    bandPaciente = False
                    print(pacientes)
                    time.sleep(2)
                    os.system("clear")

        elif opc == 2:
            os.system("clear")
            print("\tAtencion al cliente !! !")
            rutPaciente = int(input("ingrese el rut del paciente! \n"))
            for paciente in pacientes:
                if paciente[0] == rutPaciente:
                    print("\tHolaaaaaaa!", paciente[1])
                    registro = input("Motivo de la consulta?!\n")
                    while registro == "":
                        registro = input("motivo de su consulta? no puede quedar el espacio en blanco! \n")
                    paciente.append(registro)
                    print(pacientes)
                    input("Enter para continuar uwu ")

        elif opc == 3:
            os.system("clear")
            print("\tGestionar paciente! ")
            banderSubMenu = True
            while banderSubMenu:
                print("1. COnsultar datos pacientes")
                print("2.Eliminar paciente! ")
                print("3. Modificar paciente! ! ")
                print("4- Regresar al menu principal! ")
                try:
                    opc2 = int(input("ingrese su opcion por favor ! \n"))
                    if opc2 == 1:
                        print("\tConsultar datos del paciente! ")
                        rut_consultar = int(input("ingrese el rut del paciente uwu \n"))
                        paciente_encontrado = None
                        for paciente in pacientes:
                            if paciente[0] == rut_consultar:
                                paciente_encontrado = paciente
                                break
                        if paciente_encontrado:
                            print("\tPaciente encontrado!!!!!! ")
                            print("Rut:", paciente_encontrado[0])
                            print("Nombre:", paciente_encontrado[1])
                            print(f"Direccion: {paciente_encontrado[2]}")
                            print("Correo:", correo[3])
                            print("Edad:", edad[4])
                            print("Sexi: ", paciente_encontrado[5])
                            print("Prevision: ", paciente_encontrado[6])
                            print("Registro: ", paciente_encontrado[7])

                        else:
                            print("cliente no existe u.u")
                            input("presione una tecla para continuar uwu ")

                    elif opc2 == 2:
                        print("\tModificar paciente! ")
                        rut_editar = int(input("ingrese rut paciente\n"))
                        paciente_editado = None
                        for paciente in pacientes:
                            if paciente [0] == rut_editar:
                                paciente_editado = paciente
                        if paciente_editado:
                            campo = input("Ingrese el campo que desea editar! (nombre, direccion, correo, edad, sexo, prevision)")
                            if campo in ['nombre', 'direccion', 'correo', 'edad', 'sexo', 'prevision']:
                                nuevo_valor = input(f"Ingrese el valor para el campo {campo}")
                                if campo == 'edad':
                                    nuevo_valor = int(nuevo_valor)
                                    paciente_editado[4] = nuevo_valor
                                if campo == 'nombre':
                                    paciente_editado[1] = nuevo_valor
                    elif opc2 == 3:
                        print("\tEliminar pacientes! ")
                        rut_eliminar = int(input("Ingrese el rut del paciente por favor \n"))
                        for paciente in pacientes: 
                            if paciente [0] == rut_eliminar:
                                try:
                                    pacientes.remove(paciente)
                                    print("paciente eliminado con exito....")
                                    time.sleep(1)
                                except:
                                    print("rut ingresado no valido! ")
                    elif opc2 == 4:
                        print("\tRegresar al menu principal! ")
                        
                except:
                    print("opcion no valida! ")


        elif opc == 4:
            os.system("clear")
            print("\tSalir! ")
            print("Uste ha salido del sistema..... byebye ")
            banMenu = False

    except:
        print("\topcion no valida!")
        time.sleep(1)
        os.system("clear")
