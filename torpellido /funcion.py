import random
from os import system, name
import time
contado_id=1 #el contador para el id 
estudiantes = [] #la lista que enumerara todas las funciones, id, nombre, edad, comportamiento, notas, y asistencias
def menu(): #creamos una funcion para el menu
    clear()
    print("\tMenu principal!")
    print("1. Registrar Estudiante!")
    print("2. Buscar Estudiante!")
    print("3. Imprimir certificados")
    print("4.Salir\n")


def clear(): #funcion para limpiar pantalla, tanto en windows como en cualquier so
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def obtener_id(contador_id): #funcion para obtener el id, comprobar que el campo no venga vacio y cumplir con que sea solo basica o media!
    clear()
    while True:
        info = input("Ingrese el grado academico del alumno! (basica o media )\n").lower() #lower es para que todo string ingresado lo devuelva en minusculas
        if info == "basica":
            id_final = '0' + str(contador_id) + "-AB" #con esto solo vamos sumando todo, 0 + 1 + -AB = 01-AB, que es la id del estudiante!
            break
        elif info == "media":
            id_final =  '0' + str(contador_id) + "-AM"
            break
        else:
            print("Por favor indique si es de media o basica!\n")
    return id_final #devuelve el id_final

def obtener_nombre():
    clear()
    while True:
        nombre = input("Ingrese nombre y apellido del estudiante por favor!\n")
        if nombre != "" and nombre != " " and not "  " in nombre :
            if len(nombre)>=5: #ya que la condicion es que el nombre no puede contener menos de 5 caracteres, se ocupa len, para así contar las letras del string. >=5 que siosi tiene que ser mayor a 5 
                break #cumple la condicion, asi que saldrá del bucle establecido
            else:
                print("Por favor indique el nombre y apellido del alumno!")
        else:
            clear()
            print("el espacio no puede venir vacio!\n")
    return nombre #devuelve el nombre

def obtener_edad():
    clear()
    while True:
        try:
            edad = int(input("Indique la edad del estudiante por favor! tiene que ser mayor o igual a 12, y menor o igual a 18  \n"))
            if edad >=12 and edad <=18:
                print("Edad registrada correctamente!")
                break
            else:
                print("Por favor, indique la edad del estudiante! no puede ser menor de 12 años, y tampoco mayor de 18 años!")
        except:
            print("Por favor indique la edad del estudiante!")
    return edad



def registrar_estudiante():
    contador_id=1
    while True:
        id_estudiante = obtener_id(contador_id)
        contador_id=1
        nombre = obtener_nombre()
        edad = obtener_edad()
        asistencia = random.randint(1, 100)
        nota = random.randint(10,70)
        conducta = random.randint(1, 100)
        estudiante = [id_estudiante, nombre, edad, asistencia, nota, conducta]
        estudiantes.append(estudiante)
        print(estudiantes)
        enter =input("enter para continuar...")
        agregar = input("Desea agregar otro estudiante?\n1.SI\n2.NO  \n")
        if agregar == "1":
            continue
        elif agregar == "2":
            break
        else:
            print("por favor indique si desea agregar otro estudiante?")

def buscar_estudiante():
    id_buscar = input("Ingrese id del alumno a buscar!\n")
    for estudiante in estudiantes:
        if estudiante[0] == id_buscar:
            clear()
            print(f"ID: {estudiante[0]}")
            print(f"NOMBRE: {estudiante[1]}")
            print(f"EDAD: {estudiante[2]}")
            print(f"ASISTENCIA: {estudiante[3]}")
            print(f"NOTAS: {estudiante[4]/10}")
            print(f"CONDUCTA {estudiante[5]}/100\n")
            enter =input("enter para continuar...")


def imprimir_certificados():
    while True:
        clear()
        print("\tMenu de imprimir certificados!")
        print("1. Certificados asistencia")
        print("2. Certificados notas")
        print("3. Certificados conducta")
        print("4. Certificado general")
        print("5. Volver al menu principal\n ")
        opc2 = input("Ingrece opcion!\n")
        if opc2 == "1":
            id_buscar = input("Ingrese id del alumno a buscar!\n")
            for estudiante in estudiantes:
                if estudiante[0] == id_buscar: #el id al coincidir con el de un alumno, inicia el certificado de asistencia
                    clear()
                    print(f"ID: {estudiante[0]}")
                    print(f"NOMBRE: {estudiante[1]}")
                    print(f"EDAD: {estudiante[2]}")
                    enter =input=("Enter para continuar...")
                    if estudiante[3]<70: #esta funcion indica que, la asistencia al ser menos que el 70%, el alumno reprueba por inasistencia
                        print(f"La asistencia de {estudiante[1]}es de {estudiante[3]} %")
                        print("Estudiante Reprobado por baja asistencia!")
                        print(".................................")
                        enter =input("Enter para continuar...")
                    else: #caso contrario, aprueba por asistencia
                        
                        print(f"La asistencia del {estudiante[1]} es de {estudiante[3]}%")
                        print("Estudiante tiene excelente asistencia!")
                        print("""
            ⣤⢔⣒⠂⣀⣀⣤⣄⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⢠⣟⡼⣷⠼⣆⣼⢇⣿⣄⠱⣄
⠀⠀⠀⠀⠀⠀⠀⠹⣿⡀⣆⠙⠢⠐⠉⠉⣴⣾⣽⢟⡰⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠤⢴⣿⠿⢋⣴⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡙⠻⣿⣶⣦⣭⣉⠁⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⠉⠉⠉⠉⠇⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣘⣦⣀⠀⠀⣀⡴⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢻⣿⣿⣿⣿⠻⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣿⠉⠻⣇⠘⠓⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢶⣾⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⠻⢿⣿⣿⠿⠛⣄⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀""")
                        time.sleep(3)
                elif opc2 == "2":
                    id_buscar = input("Ingrese id del alumno a buscar!\n")
                    for estudiante in estudiantes:
                        if estudiante[0] == id_buscar:
                            print("\tCertificado de nota")
                            print(f"ID: {estudiante[0]}")
                            print(f"NOMBRE: {estudiante[1]}")
                            print(f"EDAD: {estudiante[2]}")
                            if estudiante[4]<40:
                                print(f"La nota de {estudiante[1]} es {estudiante[4]/10}")
                                print("Alumno Reprueba por notas!")
                                print(".................")
                                enter =input("ENter para continuar...")
                            else:
                                print(f"La nota de {estudiante[1]} es {estudiante[4]/10}")
                                print("Alumno aprueba con sus increibles notas!")
                                print(".........................")
                                time.sleep(3)
                elif opc2 == "3":
                    id_buscar = input("Ingrese id del alumno a buscar!\n")
                    for estudiante in estudiantes:
                        print("\tCertificado de conducta!")
                        print(f"ID: {estudiante[0]}")
                        print(f"NOMBRE: {estudiante[1]}")
                        print(f"EDAD: {estudiante[2]}")
                        if estudiante[5]<40:
                            print(f"La conducta de {estudiante[1]} es de {estudiante[5]}% segun profesores!")
                            print("El estudiante tiene mala conducta!")
                            time.sleep(3)


                        elif estudiante[5]>=40 and estudiante[5]<=8:
                            print(f"La conducta de {estudiante[1]} es de {estudiante[5]}% segun profesores")
                            print("El estudiante tiene buena conducta...")
                            print("....................")
                            time.sleep(3)
                        else:
                            print(f"La conducta de {estudiante[1]} es de {estudiante[5]}% segun profesores")
                            print("El estudiante tiene excelente conducta!")
                            time.sleep(3)
                elif opc2 == "4":
                    id_buscar = input("INgrese id del alumno a buscar\n")
                    for estudiante in estudiantes:
                        print("\tCertificado de general del alumno!")
                        print(f"ID: {estudiante[0]}")
                        print(f"NOMBRE: {estudiante[1]}")
                        print(f"EDAD: {estudiante[2]}")
                        print(f"ASISTENCIA {estudiante[3]}")
                        print(f"PROMEDIO: {estudiante[4]}")
                        print(f"CONDUCTA {estudiante[5]}")
                        print("""
                                ⣿⡇⠘⡇⢀⣶⣶⠄⠈⣾⡟⢂⣿⣿⣿⣿⣿⣿⡿⢉⢾⢃⣿⣿⡟⣸⢸⣿⣿⣸
                                ⣿⢸⣦⢧⢸⣿⣿⢱⠄⠄⣇⣼⣿⣿⣿⣿⣿⢟⣼⣿⡯⠸⣿⢳⢱⡏⣼⣿⢇⣿
                                ⡏⣾⢽⣼⢸⣿⣿⡘⣆⢀⠛⣿⣿⣿⣿⡿⣫⣾⣿⣿⢇⣿⠂⢌⡾⡇⣿⡿⢸⣿
                                ⢧⣿⠄⢹⢸⣿⣿⣷⣭⢸⡄⣿⣿⣿⢋⣵⣿⣿⡿⠟⡨⡡⠄⣾⣿⡆⣭⡇⣿⣿
                                ⣼⡏⡀⠄⢀⢿⣿⣿⡟⣾⡇⣿⡿⣡⢁⣿⣿⣫⡶⢃⡵⣡⣿⣮⡻⡇⣿⢸⣮⢿
                                ⣿⡇⣧⢠⠸⡎⡍⡭⢾⡏⣧⢋⢾⠏⣼⣿⣿⠿⣵⣾⣕⠿⣿⣿⣷⢡⠏⣾⣿⣿
                                ⣿⠁⣿⠈⠄⠄⢃⢹⡀⠸⢸⢿⠸⢰⢻⢿⣟⢁⣀⠄⠄⠉⠒⢝⢿⠸⣴⣿⣿⣿
                                ⡍⠇⣿⣷⢰⢰⢸⠄⡃⡆⠈⠈⡀⡌⠠⠸⠃⣿⣏⡳⢷⢄⡀⠄⠄⠰⣿⣿⣿⣿
                                ⡇⠄⠸⣿⢸⣿⣶⡄⣇⠃⡇⡄⡇⠁⠃⠄⠈⢊⠻⠿⣿⣿⣿⣦⠄⠘⣿⣿⣿⣿
                                ⡇⠄⠄⢻⣸⣿⣿⠏⡙⢸⣇⣡⢰⢀⠄⠄⠄⠈⡁⢱⢈⢿⣿⡿⡄⣰⣶⣿⣿⣿
                                ⡇⠄⠄⠄⢻⣿⡿⢰⡇⠆⠲⠶⣝⠾⠸⢴⢠⠄⠇⢸⢸⠄⡶⡜⣽⣿⣿⣿⣿⢏
                                ⠁⠄⠄⠄⠄⢿⡇⠧⢣⣸⣦⣄⣀⠁⠓⢸⣄⠸⢀⠄⡀⡀⡪⣽⣿⣿⢿⣿⢟⣬
                                ⠄⠄⠄⠄⠄⠈⢧⠯⢸⣿⣿⣿⡿⠰⣷⠄⣿⣇⡿⠄⡀⠦⣰⣿⡿⣱⣿⡏⢾⣫
                                ⠄⠄⠄⠄⠄⠄⠈⣌⢌⢿⣿⣿⠇⠼⢃⢠⢇⣻⣧⣿⡡⣸⣿⠿⢁⡟⢁⣳⣿⣿
                                ⠄⠄⠄⠄⠄⠄⠄⠄⠳⢝⣒⣒⠰⣘⣴⡧⠿⣿⣛⡯⣱⡿⣫⢎⣪⣎⣿⣧⢻⠿
                                """)
                        time.sleep(3)
                elif opc == "5":
                    print("Usted ha salido del sistema!\n")
                else:
                    print("Opcion ingresada no es valida!")
                    print("Volviendo al menu principal..\n")
                    break


def salir():
    print("Usted ha salido del sistema... que tenga un lindo diaa")
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠋⠉⠉⠳⡴⠒⠒⠒⠲⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⠀⡴⠚⡩⠟⠓⠒⡖⠲⡄⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⢠⠒⠾⢥⣀⣇⣚⣹⡤⡟⠀⡇⢠⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⣀⠀⡇⠀⠀⠀⠀⠀⢀⡜⠁⣸⢠⠎⣰⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡍⠀⠉⠉⠛⠦⣄⠀⢀⡴⣫⠴⠋⢹⡏⡼⠁⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡽⣄⠀⠀⠀⠀⠈⠙⠻⣎⡁⠀⠀⣸⡾⠀⠀⠀⠀⣀⡹⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠉⠓⠶⢟⠀⢀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠒⠦⡀⠙⠦⣀⠀⠀⠀⠀⠀⠀⢀⣴⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣀⠈⠓⣦⣤⣤⣤⢶⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣤⣤⡤⠤⠤⠤⠤⣌⡉⠉⠁⠀⠀⢸⢸⠁⡠⠖⠒⠒⢒⣒⡶⣶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⣍⠓⠦⣄⠀⠀⠙⣆⠀⠀⠀⡞⡼⡼⢀⣠⠴⠊⢉⡤⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠈⠙⢦⡀⢸⡀⠀⢰⢣⡧⠷⣯⣤⠤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⣲⠤⠬⠿⠧⣠⢏⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠉⠉⢉⣳⣄⣠⠏⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣟⣒⣋⣉⣉⡭⠟⢡⠏⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⢀⠏⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠓⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")