import os, time
import random as rd
contador_id=1
estudiantes = []

#funcion limpieza de pantalla
def limpiar_pantalla():
    os.system("cls")

def contener_id(contador_ids):
    info = input("ingrese grado academico: basica o media \n").lower()
    while info not in ['basica', 'media']:
        info = input("ingrese grado academico. Basica o Media\n").lower()
    info_id = 'AB' if info == "básica" else 'AM'
    id_final = '0' + str(contador_ids) + "-" + info_id
    contador_ids += 1
    return id_final

def obtener_nombre():
    nombre_estudiante = input("ingrese un nombre y apellido\n").lower()
    while len(nombre_estudiante) < 5:
        nombre_estudiante = input("ingrese nombre y apellido\n").lower()
    return nombre_estudiante

def obtener_edad():
    while True:
        try:
            edad_estudiante = int(input("ingrese edad\n"))
            if edad_estudiante>=12 and edad_estudiante<=18:
                print(edad_estudiante)
                break
            else:
                print("La edad debe ser mayor o igual a 12! o menor a 18")
        except:
            print("campo solo acepta valores numericos")
    return edad_estudiante

def registrar_estudiante():
    contador_ids = 1
    while True:
        id_estudiante = contener_id(contador_ids)
        contador_ids += 1
        nombre = obtener_nombre()
        edad = obtener_edad()
        asistencia = rd.randint(1, 100) 
        notas = rd.randint(10, 70)
        conducta = rd.randint(1, 100)
        estudiante = [id_estudiante, nombre, edad, asistencia, notas, asistencia]
        estudiantes.append(estudiante)
        print(estudiante)
        input("ingrese tecla\n")
        agregar = input("Desea agregar otro estudiante? 1.SI  2.NO\n")
        if agregar == "1":
            continue
        elif agregar == "2":
            break
        else:
            print("opcion invalida, intente de nuevo!")


def buscar_estudiante():
    print("Buscar datos del estudiante")
    id_buscar = input("ingrese el id que desea buscar\n").upper()
    encontrado = False
    for estudiante in estudiantes:
        if estudiante[0] == id_buscar:
            encontrado = True
            print("nombre:", estudiante[1])
            print("Edad:", estudiante[2])
            print("Conducta:", estudiante[3])
            print("Notas: ", estudiante[4])
            print("Asistencia: ", estudiante[5])
            #seguir poniendole la informacion como asistencia o conducta irrespetuosa <3
            break
    if not encontrado:
            print("Id fuera de la base de datos")
    time.sleep(3)

def obtener_asistencia():
    asistencia = rd.radiant(1, 100)
    if asistencia < 70:
        print(f"Alumno reprueba por inasistencia: {asistencia}%")
    else:
        print(f"El alumno no reprueba por asistencia: {asistencia}%")
    estudiantes.append(asistencia)
    return asistencia

def obtener_notas():
    notas = rd.randint(1, 70)
    if notas < 40:
        print(f"El alumno reprueba por notas {notas}")
    else:
        print(f"El Alumno aprueba: {notas}")
    estudiantes.append(notas)
    return notas

def obtener_conducta():
    conducta = rd.radiant(1, 100)
    if conducta < 70:
        print(f"Alumno reprueba por conducta: {conducta}")
    else:
        print(f"Alumnno aprueba por conducta: {conducta}")
    estudiantes.append(conducta)
    return conducta

def imprimir_menu():
    limpiar_pantalla()
    print("1) Registrar Estudiante")
    print("2) Buscar Estudiantes")
    print("3) Imprimir Certificados")
    print("4) Salir")

def salir():
    limpiar_pantalla()
    print("Saliendo")
    time.sleep(3)


def imprimir_certificado():
    while True: #el bucle XD
        print("Menu imprimr certificado")
        print("(1) Certificados asistencia")
        print("(2) Certificados nota")
        print("(3) Certificados conducta")
        print("(4) Volver al menu principal")
        opc2 = input("ingrese opcion\n") #hacemo un submenu para las nuevas funciones uwu aqui va lo de si el wn aprueba o reprueba 
        if opc2 == "1":
            id_buscar = input("ingrese id del alumno a buscar\n")
            for estudiante in estudiantes: #el for es para buscar el estudiante dentro de la lista estudiantes
                if  estudiante[0] == id_buscar: #esto es pa identificar el id del alumno uwu x eso es [0] ya que ahí se encuentra el orden del id 
                    print("-------CERTIFICADO DE ASISTENCIA-------")
                    print("ID:", estudiante[0]) #para imprimir id
                    print("NOMBRE:", estudiante[1]) #imprimir nombre
                    print("EDAD:", estudiante[2]) #imprimir edad
                    if estudiante[3]<70: #aqui al ser una funcion random, tienes que crear varias posibilidades, si es menor al 70 reprueba
                        print(f"La asistencia de {estudiante[1]} es de {estudiante[3]}%")
                        print("REPROBADO POR BAJA ASISTENCIA ")
                        print("---------------------------------------")
                    else:
                        print(f"La asistencia de {estudiante[1]} es de {estudiante[3]}%") #esto es el caso contrario xd si saca mayor aprueba obvio 
                        print("APROBADO POR BUENA ASISTENCIA")
                        print("---------------------------------------")
        elif opc2 == "2":
            id_buscar = input("ingrese id del alumno a buscar\n")
            for estudiante in estudiantes:
                if  estudiante[0] == id_buscar: 
                    print("-------CERTIFICADO DE NOTA-------")
                    print("ID:", estudiante[0])
                    print("NOMBRE:", estudiante[1])
                    print("EDAD:", estudiante[2])
                    if estudiante[4]<40:
                        print(f"La nota de {estudiante[1]} es {estudiante[4]/10}") #esto lo mismo de la asistencia. el random es aleatorio asi que jiji
                        print("ESTUDIANTE REPROBADO")
                        print("---------------------------------------")
                    else:
                        print(f"La nota de {estudiante[1]} es {estudiante[4]/10}")
                        print("ESTUDIANTE APROBADO")
                        print("---------------------------------------")
        elif opc2 == "3":
            id_buscar = input("ingrese id del alumno a buscar\n")
            for estudiante in estudiantes:
                if  estudiante[0] == id_buscar:
                    print("-------CERTIFICADO DE ASISTENCIA-------")
                    print("ID:", estudiante[0])
                    print("NOMBRE:", estudiante[1])
                    print("EDAD:", estudiante[2])
                    if estudiante[5]<40:
                        print(f"La conducta de {estudiante[1]} es de {estudiante[5]}%")
                        print("EL ESTUDIANTE TIENE MALA CONDUCTA")
                        print("---------------------------------------")
                    elif estudiante[5]>=40 and estudiante[5]<=80: #un vio el compa
                        print(f"La conducta de {estudiante[1]} es de {estudiante[5]}%")
                        print("EL ESTUDIANTE TIENE BUENA CONDUCTA")
                        print("---------------------------------------")
                    else:
                        print(f"La conducta de {estudiante[1]} es de {estudiante[5]}%") #este qlo es capo
                        print("EL ESTUDIANTE TIENE EXELENTE CONDUCTA")
                        print("---------------------------------------")
        elif opc2 == "4":
            print("Saliendo al menu principal...\n")
            break
        else:
            print("opcion ingresada no es valida")
            print("volviendo al menu principal...\n")
            break
