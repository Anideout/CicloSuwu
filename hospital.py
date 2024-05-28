import time, os
centroMedico = True
os.system("cls")
while centroMedico:
    print("\t\tCentro Médico DUOC\n")
    print("1. Registrar Paciente! ")
    print("2. Atención Paciente! ")
    print("3. Gestionar Paciente! ")
    print("4. Salir")
    try:
        opc = int(input("\tIngrese su opcion !!! \n"))
        if opc == 1:
            print("\t Registrar Paciente ! ")
            banRut = True
            while banRut:
                try:
                    rut = int(input("ingrese su rut por favor, sin agregar el digito verificador !\n"))
                    if rut <= 5000000 or rut >= 99999999:
                        rut = int(input("Ingrese su rut correctamente! recuerde que es sin numero verificador \n"))
                    banRut = False
                except:
                    print("Rut ingresado no valido! ")
            banNombre = True
            while banNombre:
                try:
                    nombre = input("indique cual es su nombre por favor ! \n")
                    if nombre == "" or nombre == " ":
                        nombre = input("ingrese su nombre por favor, no puede quedar el espacio en vacio! ")
                except:
                    print("")
            banEdad = True
            while banEdad:    
                edad = int(input("\tIngrese su edad porfavor ! \n"))
                if edad < 0 or edad > 110:
                    edad = int(input("Ingrese su edad correctamente! recuerde que tiene que estar dentro del rango de 0 a 110\n"))
                banEdad = False
            correo = input("Ingrese su correo electronico por favor (recuerde que debe contener un @ para que sea valido ! \n")
            while '@' not in correo:
                correo = input("ingrese su correo nuevamente, recuerde que debe contener un @ para que sea valido ! \n")
                
            sexo = input("ingrese su preferencia sexual por favor ! indiquelo con una F o una M, o con NB \n")
            while sexo == "f" or sexo == "m" or sexo == "nb" or sexo == "F" or sexo == "M" or sexo == "NB":
                sexo = input("ingrese su preferencia sexual bien por favor.. \n")
                
            ps = input("indique prevision de salud!: \n")
            while ps == "ISAPRE" or ps == "FONASA" or ps == "isapre" or ps == "FONASA":
                ps = input("indique nuevamente por favor, usted es medio menso pa la wea \n")
                
                
        elif opc == 2:
            print("\tAtencion paciente! ")
            rutPaciente = int(input("ingrese el rut del paciente por favor \n"))
            
                
            
            
    except:
        print("opcion no valida! ")