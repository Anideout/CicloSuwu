from os import system, name
import time
estudiantes = []
def clear():
    if name == 'nt':
        _ = system('cls')
        
    else:
        _ = system('clear')
     


def menu():
    clear()
    print("\tBienvenido a liceano!!")
    print("1.Registrar Estudiante!")
    print("2. Buscar estudiante!")
    print("3. Imprimir Certificado! ")
    print("4. Salir")
    
  
def obt_id(contador_ids):
    info = input("Ingrese grado academico basica o media\n").lower()
    while info not in ['basica', 'media']:
        info = input("Ingrese grado academico basica o media! \n").lower
        
    if info == "basica":
        info_id = 'AB'
        
    elif info == "media":
        info_id = 'AM'
    
    else:
        print("Por favor indique si es de media o basica, no es posible mas opciones! ")
    id_final = '0' + str(contador_ids)+ "-" + info_id
    contador_ids += 1
    agregar = input("Desea agregar otro alumno? indique con \n1.SI \t2.NO\n")
    return id_final            
                
def obt_nombre():
    banNombre = True
    while banNombre:
        nombre = input("\tPor favor ingrese su nombre! \n")
        if len(nombre) > 5:
            print("\tNombre ingresado correctamente! ")
            banNombre = False
        else:
            print("Por favor indique su nombre! no puede contener menos de 5 caracteres! ")
    return obt_nombre
            


        
      
def obt_edad():
    
    while True:
        
        try:
            edad = int(input("Ingrese su edad por favor!\n"))
            while not edad or edad <= 18 or edad >= 12:
                edad = int("Ingrese su edad por favor! \n") 
            break
            
        except:
            print("la edad ingresada no es valida! intente de nuevo por favor! ")
    return edad
      
import random as rd
asistencias = []
def obt_asistencia():
    while True:
        asistencia = rd.randint(1, 100)
        if asistencia < 70:
            print(f"Alumno reprueba por inasistencia! {asistencia}%")
            
        else:
            print(f"Alumno no reprueba por inasistencia! {asistencia}%")
        asistencia.append(asistencia)
        seguir = input("Desea agregar otra asistencia?    1.Si    2.No")
        if seguir == 1: 
            continue
        elif seguir == 2:
            break
        print(asistencia)
        
        
def registrar_alumno():
    contador_ids = 1
    while True:
        ID_Estudiante = obt_id(contador_ids)
        contador_ids += 1
        nombre = obt_nombre()
        edad = obt_edad()
        estudiante = [ID_Estudiante, nombre, edad]
        estudiantes.append(estudiante)
        print(estudiantes)
        input("enter para continuar...")
        try:
            otro_alumno = int(input("Desea agregar otro alumno? indique con:     \n1.SI   \t\n2.NO\n"))
            while not otro_alumno:
                otro_alumno = int(input("Desea agregar otro alumno? \n1.Si  \t\n2.NO\n")).lower()
                while otro_alumno not in ['si', 'no']:
                    otro_alumno = input("Desea agregar otro estudiante? 'si  no").lower()
                    
            if otro_alumno !=2:
                continue
            else:
                break
            
        except:
            print("opcion no valida! intente de nuevo por favor! ")
            
def salir():
    clear()
    print("Saliendo del sistema\n.\t\n.\t\t\n. \t\t\t\n.")
    time.sleep(2)
    
    
    
def buscar_alumno():
    clear()
    print("\nBuscar alumno!")
    id_buscarr = input("Ingrese rut del alumno a buscar! \n")
    for estudiante in estudiantes:
        if estudiante[0] == id_buscarr:
            print(f"ID: \n{estudiante[0]}")
            print(f"NOMBRE: \n{estudiante[1]}")
            print(f"EDAD: \n{estudiante[2]}")
        input("Enter para continuar... ")
        



            
        