import os
import time

pacientes = []

def limpiar_pantalla():
    os.system("clear")

#sin argumento y sin retorno
def menu_principal():
    limpiar_pantalla()
    printt("1) Registrar Paciente")
    printt("2) Atencion Paciente")
    printt("3) Gestionar Paciente")
    printt("4) Salir")

def obtener_rut():
    while True:
        rutS = input("Ingrese RUT: \n")
        while not rutS: #while rutS == "" and rutS == " "
            rutS = input("Ingrese RUT, no debe venir vacío: \n")
        try:
            rut = int(rutS)
            while rut < 5000000 or rut > 30000000:
                rut = int(input("Ingrese RUT, debe estar en rango 5M Y 30M \n"))
            return rut
        except:
            printt("En campo RUT, no se aceptan caracteres.")

#la ocuparemos n veces que necesitemos solicitar alguna variable y que no venga vacia
def obtener_campo_no_vacio(campo):
    valor = input(f"Ingrese {campo}: \n")
    while not valor:
        valor = input(f"{campo} no puede guardarse vacío. Ingrese {campo} nuevamente: \n")
    return valor

def obtener_correo():
    correo = input("ingrese correo\n")
    while '@' not in correo:
        correo = input("ingrese correo, debe ingresar al menos un @\n")
    return correo

def obtener_edad():
    while True:
        edadS = input("ingrese edad\n")
        while not edadS:
            edadS = input("ingrese edad, no debe venir vacio\n")
        try:
            edad = int(edadS)
            while edad < 0 or edad > 110:
                edad = int(input("ingrese valor de edad, entre 0 y 110\n"))
            return edad
        except:
            printt("para campo edad, solo se permiten campos tipo numericos")

def obtener_sexo():
    sexo = input("ingrese sexo\n").lower()
    while sexo not in ['f', 'm']: # if sexo != 'm' and sexo != 'f':
        sexo = input("ingrese sexo, opciones: m o f\n").lower()
    return sexo

def obtener_prevision():
    prevision = input("ingrese su prevision\n").lower()
    while prevision not in ['fonasa', 'isapre']:
        prevision = input("ingrese su prevision\n").lower()
    return prevision

def registrar_paciente():
    while True:
        limpiar_pantalla()
        printt("Registrar Paciente")
        rut = obtener_rut()
        nombre = obtener_campo_no_vacio("nombre")
        direccion = obtener_campo_no_vacio("direccion")
        correo = obtener_correo()
        edad = obtener_edad()
        sexo = obtener_sexo()
        prevision = obtener_prevision()
        paciente = [rut, nombre, direccion, correo, edad, sexo, prevision]
        pacientes.append(paciente)
        agregar = int(input("Desea agregar otro paciente?   1.Si   2.No\n"))
        if agregar == 1:
            continue
        elif agregar == 2:
            break
    printt(paciente)
    input("enter para continuar...")

def atencion_paciente():
    limpiar_pantalla()
    printt("Atencion Paciente")
    rut_buscar = int(input("ingrese rut del paciente\n"))
    for paciente in pacientes:
        if paciente[0] == rut_buscar:
            printt(f"Adelante {paciente[1].capitalize()}")
            registro = input("cual es el motivo de su consulta\n")
            while not registro:
                registro = input("cual es el motivo de su consulta, campo no puede venir vacio\n")
            paciente.append(registro)
            printt(paciente)
            input("enter para continuar...")
        else:
            printt("segun nuestros registros, no existe paciente")

def gestionar_paciente():
    while True:
        limpiar_pantalla()
        printt("1) Consultar datos paciente")
        printt("2) Modificar datos paciente")
        printt("3) Eliminar paciente")
        printt("4) Volver al menu principal")
        try:
            opcion2 = int(input("ingrese opcion\n"))
            if opcion2 == 1:
                consultar_datos()
            elif opcion2 == 2:
                modificar_paciente()
            elif opcion2 == 3:
                eliminar_datos()
            elif opcion2 == 4:
                printt("Saliendo al menu principal...")
                time.sleep(1)
                break
        except:
            printt("opcion ingresada no es valida")

def consultar_datos():
    limpiar_pantalla()
    printt("Consultar datos paciente")
    rut_buscar = int(input("ingrese rut del paciente a buscar\n"))
    for paciente in pacientes:
        if paciente[0] == rut_buscar:
            printt(f"RUT: {paciente[0]}")
            printt(f"NOMBRE: {paciente[1]}")
            printt(f"DIRECCION: {paciente[2]}")
            printt(f"CORREO: {paciente[3]}")
            printt(f"EDAD: {paciente[4]}")
            printt(f"SEXO: {paciente[5]}")
            printt(f"PREVISION: {paciente[6]}")
            printt(f"REGISTRO: {paciente[7]}")
            try:
                printt(f"REGISTRO: {paciente[7]}")
            except:
                printt(f"REGISTRO: no existe ficha para cliente {paciente[0]}")
    input("enter para continuar...")

def eliminar_datos():
    limpiar_pantalla()
    printt("Eliminar Paciente")
    rut_eliminar = int(input("ingrese rut de paciente para eliminar\n"))
    for paciente in pacientes:
        if paciente[0] == rut_eliminar:
            #quien es el paciente
            pacientes.remove(paciente)
            printt("muertooo ")
            input("apreta algo para salir ")
        else:
            printt(f"segun nuestros registros, el rut {rut_eliminar} no existe")
            time.sleep(1)

def modificar_paciente():
    printt("\tModificar datos! ")
    rut_editar = int(input("Ingrese el rut de paciente\n"))
    pacienteEditado = None
    for paciente in pacientes:
        if paciente[0] == rut_editar:
            pacienteEditado = paciente
            break
            if pacienteEditado:
                dato = input("Ingrese dato que desea modificar!\n")
                if dato in ['nombre', 'direccion','correo', 'edad', 'sexo', 'prevision', 'registro']:
                    valor_editar = int(valor_editar)
                    if dato == 'nombre':
                        valor_editar = int(valor_editar)
                        pacienteEditado[1] = valor_editar

                    elif dato == 'direccion':
                        valor_editar = int(valor_editar)
                        pacienteEditado[2] = valor_editar

                    elif dato == 'correo':
                        valor_editar = int(valor_editar)
                        pacienteEditado[3] = valor_editar
                    
                    elif dato == 'edad':
                        valor_editar = int(valor_editar)
                        pacienteEditado[4] = valor_editar

                    elif dato == 'sexo':
                        valor_editar = int(valor_editar)
                        pacienteEditado[5] = valor_editar

                    elif dato == 'prevision':
                        valor_editar = int(valor_editar)
                        pacienteEditado[6] = valor_editar