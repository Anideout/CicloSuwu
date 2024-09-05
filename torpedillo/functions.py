import random, time, os

estudiantes = []
#id autoincremental, debe venir en formato 01-AB o 01-AM
def limpiar():
    os.system("cls")
    
def obtener_id(contador_ids):
    info = input("ingrese grado academico basica o media\n").lower()
    while info not in ['basica', 'media']:
        info = input("ingrese grado academico basica o media\n").lower()
    if info == "basica":
        info_id = 'AB'
    elif info == "media":
        info_id = 'AM' 
    id_final = '0' + str(contador_ids)+ "-" + info_id
    contador_ids += 1
    return id_final      

def obtener_nombre():
    nombre_estudiante = input("ingrese nombre y apellido\n")
    while len(nombre_estudiante) < 5:
        nombre_estudiante = input("ingrese nombre y apellido\n")
    return nombre_estudiante

def obtener_edad():
    while True:
        try:
            edad_estudiante = int(input("ingrese edad\n"))
            while not edad_estudiante or edad_estudiante < 12 or edad_estudiante > 18:
                edad_estudiante = int(input("ingrese edad \n"))
            break
        except:
            print("campo edad solo acepta valores numericos")
    return edad_estudiante


def registrar_estudiante():
    contador_ids = 1
    while True:
        id_estudiante = obtener_id(contador_ids)
        contador_ids += 1
        nombre = obtener_nombre()
        edad = obtener_edad()
        estudiante = [id_estudiante, nombre, edad]
        estudiantes.append(estudiante)
        print(estudiantes)
        input("...")
        try:
            otro_estudiante = int(input("desea agregar otro estudiante? 1.si  2.no\n"))
            while not otro_estudiante:
                otro_estudiante = input("desea agregar otro estudiante? 'si  no'\n").lower()
                while otro_estudiante not in ['si', 'no']:
                    otro_estudiante = input("desea agregar otro estudiante? 'si  no'\n").lower()
            if otro_estudiante !=2:
                continue
            else:
                break
            
        except:
            print("solo acepta como opcion 1.si  y 2.no")
        
def imprimir_menu():
    print("1) Registrar Estudiante")
    print("2) Buscar Estudiante")
    print("3) Imprimir Estudiante")
    print("4) Imprimir Certificados")
    print("5) Salir")
    
def salir():
    limpiar()
    print("saliendo.")
    time.sleep(1)
    limpiar()
    print("saliendo..")
    time.sleep(1)
    limpiar()
    print("saliendo...")
    time.sleep(1)
    
def buscar_alumno():
    clear()
    print("\nBuscar alumno!")
    id_buscarr = input("Ingrese i del alumno a buscar! \n")
    for estudiante in estudiantes:
        if estudiante[0] == id_buscarr:
            print(f"ID: \n{estudiante[0]}")
            print(f"NOMBRE: \n{estudiante[1]}")
            print(f"EDAD: \n{estudiante[2]}")
        input("Enter para continuar... ")
        