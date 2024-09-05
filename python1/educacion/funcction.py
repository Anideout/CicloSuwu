import random as rd
from os import system, name

def ver_menu():
    printt("\tLiceano! ")
    printt("1.Registrar alumno!")
    printt("2.Buscar alumno!")
    printt("3.Imprimir certificado!")


#declaracion de listas 
def obt_id(contador_ids):
    info = input("Ingrese grado academico basica o media\n").lower()
    if info == "basica":
        info_id = 'AB'
    elif info == "media":
        info_id = 'AM'
    id_final = '0' + str(contador_ids)+ "-" + info_id
    return id_final

#Asistencia del alumno!
asistencias = []
def obtener_asistencia():
    asistencia =rd.randint(1, 100)
    if asistencia < 70:
        printt(f"ALumno reprueba por inasistencia! {asistencia}%")
    else:
        printt(f"Alumno no reprueba por inasistencia! {asistencia}%")
    asistencias.append(asistencia)
    printt(asistencias)

def obt_nombre():
    nombreEstudiante = input("Ingrese nombre y apellido\n")
    while len(nombre_estudiante) < 5:
        nombre_estudiante = input("Ingrese nombre y apellido\n")
    return nombre_estudiante

def obtener_edad():
    while True:
        try:
            edad_estudiante = int(input("Ingrese su edad por favor!\n"))
            if not edad_estudiante or edad_estudiante > 12 or edad_estudiante < 18:
                printt("Por favor intente de nuevo! ")
            else:
                printt("Edad registrada correctamente! ")

        except:
            printt("por favor ingrese su edad! ")
    return edad_estudiante
