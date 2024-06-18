from os import system, name
import time, random as rd
def clear():
    if name == 'nt':
        _ = system('cls')
        
    else:
        _ = system('clear')
     

        
def menu():
    print(" \t\tBienvenido a liceano!!")
    print("1.Registrar Estudiante!")
    print("2. Buscar estudiante!")
    print("3. Imprimir Certificado! ")
    print("\t\t4. Salir")
    
  

def obt_id():
    while True:
        idS = input("Ingrese grado academico basica o media \n").lower()
        while not idS:
            idS = input("Ingrese grado academico basica o media por favor! no puede quedar el espacio en vacio").lower()
            
        try:
            id = int(idS)
            if id == "basica":
                info_id = 'AB'
            elif id == 'media':
                info_id = 'AM'
            
            else:
                print("Por favor intentelo de nuevo, ha ingresado un caracter erroneo ! ")
            
            id_final = 00 + str(contador_ids)+ "-" + info_id
        
        
        except:
            print("error, por favor intentelo de nuevo ")
            
            
def obt_campovacio():
    
    while True:
        
        nombre = input("Ingrese su nombre por favor! \n")
        if nombre < 5 and nombre == "":
            print("Su nombre no es valido! debe ser minimo 5 caracter! ")
            
        elif:
            return nombre

        
      
def obt_edad():
    edadS = input("Ingrese su edad por favor! debe ser mayor o igual a 12, y menor o igual a 18!\n")
    while not edadS:
        edadS = input("Ingrese su nombre por favor! no puede tener el espacio vacio por faovR! \n")
    try:
        
    except:
        print("la edad ingresada no es valida! intente de nuevo por favor! ")
        
      

def obt_asistencia():
    while True:
        asistencia = random.randint(1, 100)
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

            

            
        