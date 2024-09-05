from os import system, name 
def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


pacientes = []


def menu_principal():
    clear()
    printt("\t\tBienvenido a la clinica davilaaa!!")
    printt("1. Registrar paciente!")
    printt("2. Atencion Paciente")
    printt("3. Gestionar Paciente")
    printt("4. Salir ")

def obt_rut():
    while True:
        rutS = input("Ingrese su rut por favor! \n")
        while not rutS:
            rutS = input("Ingrese bien su rut, recuerde que el campo no debe venir vacio! \n")
        try:
            rut = int(rutS)
            while rut < 5000000 or rut > 30000000:
                rut = int(input("Ingrese RUT, debe estar en rango 5M y 30M \n"))
            return rut
        except:
            printt("Su rut no es valido, no se aceptan caracteres! !")


def obt_campovacio(campo):
    valor = input(f"Ingrese {campo}: \n")
    while not valor:
        valor = input(f"{campo} no puede guardarse vacío. Ingrese {campo} nuevamente!: \n")
    return valor

def obt_correo():
    correo = input("Ingrese su correo por favor! \n")
    while '@' not in correo:
        correo = input("Ingrese su correo bien por favor, recuerde que debe contener al menos un @ para poder ser valido!\n")
    return correo

def obt_edad():
    banEdad = True
    while banEdad:
        edadS = input("Ingrese su edad por favor! ")
        while not edadS:
            edadS = input("Ingrese su edad por favor! no debe venir vacio\n")
        try:
            edad = int(edadS)
            while edad < 0 or edad > 110:
                edad = int(input("Ingrese su edad por favor, asegurese de cumplir con el rango!\n"))
            return edad
        except:
            printt("para campo edad, solo se permiten campos tipo numericos!")

def obt_genero():
    sexo = input("Ingrese sexo\n").lower()
    while sexo not in ['f', 'm']:
        sexo = input("INgrese sexo, opciones: m o f \n").lower()
    return sexo 

def obt_prevision():
    prevision = input("Indique su prevision! \n").lower()
    while prevision not in ['fonasa', 'isapre']:
        prevision = input("Indique si es fonasa o isapre! \n").lower()
    return prevision 

def registrar_paciente():
    while True:
        clear()
        printt("Registrar paciente! ")
        rut = obt_rut()
        nombre = obt_campovacio('nombre')
        direccion = obt_campovacio("direccion")
        correo = obt_correo()
        edad = obt_edad()
        sexo = obt_genero()
        prevision = obt_prevision()
        paciente = [rut, nombre, direccion, correo, edad, sexo, prevision]
        pacientes.append(paciente)
        agregar = int(input("Desea agregar otro paciente? indique con:     \n1.Si     \n2.No \n"))
        if agregar == 1:
            continue
        elif agregar == 2:
            break
        else:
            printt("Usted ha ingresado una opcion no valida! ")

    printt(paciente)
    input("Enter para continuar...")


def atencion_paciente():
    clear()
    printt("Atencion paciente!")
    rut_buscar = int(input("Ingrese rut del paciente!"))
    for paciente in pacientes:
        if paciente[0] == rut_buscar:
            printt(f"Adelante don {paciente[1].capitalize()}")
            registro = input("Cual es el motivo de su consulta? ")
            while not registro:
                registro = input("Cual es el motivo de su consulta?!")
            paciente.append(registro)
            printt(paciente)
            input("Enter para continuar... ")
        else:
            printt("Segun nuestros registros, no existe paciente! ")

def gestionar_paciente():
    while True:
        clear()
        printt("1. Consultar datos paciente")
        printt("2. Modificar datos del paciente! ")
        printt("3. ELiminar paciente! ")
        printt("4. Volver al menu principal")
        try:
            opc2 = int(input("Ingrese opcion! \n"))
            if opc2 == 1:
                consultar_datos()
            elif opc2 == 2:
                modificar_paciente()
            elif opc2 == 3:
                eliminar_datos()
            elif opc2 == 4:
                printt("Saliendo al menu principal...")
                time.sleep(1)
                break
        except:
            printt("Opcion ingresada no es valida! ")

def consultar_datos():
    clear()
    printt("Consultar datos paciente! ")
    rut_buscar = int(input("Ingrese rut del paciente a buscar! \n"))
    for paciente in pacientes:
        if paciente[0] == rut_buscar:
            printt(f"RUT: {paciente[0]}")
            printt(f"NOMBRE: {paciente[1]}")
            printt(f"DIRECCION: {paciente[2]}")
            printt(f"CORREO: {paciente[3]}")
            printt(f"EDAD: {paciente[4]}")
            printt(f"SEXO: {paciente[5]}")
            printt(f"PREVISION: {paciente[6]}")
            try:
                printt(f"REGISTRO: {paciente[7]}")
            except:
                printt("REGISTRO: no existe ficha para cliente {paciente[0]}")
    input("Enter para continuar! ")

def eliminar_datos():
    clear()
    printt("Eliminar Paciente")
    rut_eliminar = int(input("Ingrese rut del paciente por favor! "))
    for paciente in pacientes: 
        if paciente[0] == rut_eliminar:
            #quien chota es el paciente
            pacientes.remove(paciente)
            printt("Muertoo u.u")
            input("Enter para volver al menu principal! ")

        else:
            printt(f"Segun nuestro registros, el rut {rut_eliminar} no existe:((")
            time.sleep(1)

def modificar_paciente():
    printt("\tModificar datos! ")
    rut_editar = int(input("Ingrese el rut de paciente! \n"))
    pacienteEditado = None
    for paciente in pacientes:
        if paciente[0] == rut_editar:
            pacienteEditado = paciente
            break
            if pacienteEditado:
                dato = input("Ingrese dato que desea modificar!\n")
                if dato in ['nombre', 'direccion', 'correo', 'sexo', 'prevision', 'registro']:
                    valor_editar = int(valor_editar)
                    if dato == 'nombre':
                        valor_editar = int(valor_editar)
                        pcaienteEditado[1] = valor_editar
                    
                    elif dato == 'direccion':
                        valor_editar = it(valor_editar)
                        pacienteEditado[2] = valor_editar  

                    elif dato == 'correo':
                        valor_editar = int(valor_editar)
                        pacienteEditado[3] = valor_editar

                    elif dato == 'edad':
                        valor_editar[4] = valor_editar


                    elif dato == 'sexo':
                        valor_editar[5] = valor_editar

                    elif dato == 'prevision':
                        valor_editar = int(valor_editar)
                        pacienteEditado[6] = valor_editar

                    else:
                        printt("Ha ingresado un dato que no existe, por favor intentelo de nuevo! ")

    input("enter para continuar! ")
