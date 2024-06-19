import random
#id autoincremental, debe venir en formato 01-AB o 01-AM
def obtener_id(contador_ids):
    info = input("ingrese grado academico basica o media\n").lower()
    if info == "basica":
        info_id = 'AB'
    elif info == "media":
        info_id = 'AM' 
    id_final = '0' + str(contador_ids)+ "-" + info_id
    return id_final      

#funcion para  obtener un entero de manera aleatoria y guardarlo 
import random as rd
asistencias = []
def obtener_asistencia():
    asistencia = rd.randint(1, 100)
    if asistencia < 70:
        print(f"alumno reprueba por inasistencia: {asistencia}%")
    else:
        print(f"alumno no reprueba por inasistencia: {asistencia}%")
    asistencias.append(asistencia)
    print(asistencias)