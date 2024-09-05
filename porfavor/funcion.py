import random, csv
from os import system, name
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
sueldos = []
registros = []

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():
    printt("1. Asignar sueldos al azar!")
    printt("2. Clasificar sueldos")
    printt("3. Ver estadisticas.")
    printt("4. Reporte de sueldos ")
    printt("5. Salir del programa!\n")
    
    
def sueldos_aleatorios():
    clear()
    for trabajador in range(len(trabajadores)):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
        printt(f"{trabajadores[trabajador]}\tsueldo: {sueldo}")
    input("enter para continuar\n")


def clasificar_sueldos():
    clear()
    sueldos_bajos = []
    sueldos_medios =[]
    sueldos_altos = []
    
    for x in range(len(sueldos)):
        if sueldos[x] < 800000:
            sueldos_bajos.append((trabajadores[x], sueldos[x]))
        elif sueldos[x] >= 800000 and sueldos[x] < 2000000:
            sueldos_medios.append((trabajadores[x], sueldos[x]))
        else:
            sueldos_altos.append((trabajadores[x], sueldos[x]))
    printt("Sueldos menores a $800.000")
    printt(f"TOTAL: {len(sueldos_bajos)}")
    printt("Nombre empleado\tSueldo")
    for empleado, sueldo in sueldos_bajos:
        printt(f"{empleado}\t{sueldo}")
    
    printt("\nSueldos entre $800.000 y $2.000.000")
    printt(f"TOTAL: {len(sueldos_medios)}")
    printt("Nombre empleado\tSueldo")
    for empleado, sueldo in sueldos_medios:
        printt(f"{empleado}\t{sueldo}")
    
    printt("\nSueldos mayores a $2.000.000")
    printt(f"TOTAL: {len(sueldos_altos)}")
    printt("Nombre empleado\tSueldo")
    for empleado, sueldo in sueldos_altos:
        printt(f"{empleado}\t{sueldo}")
    input("enter para continuar")
    
def ver_estadisticas():
    valor_pequeno = sueldos[0]
    valor_grande = sueldos[0]
    ind_peq = 0
    ind_gran = 0
    multi = 1
    mayor_sueldo = max(sueldos)
    menor_sueldo = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    # print(f"el sueldo mayor es de ${mayor_sueldo}")
    # print(f"El sueldo menor es de {menor_sueldo}\n")
    # print(f"El promedio de los sueldos es de{round(promedio)}")
    # input("enter para continuar")
    
    for x in range(len(trabajadores)):
        if sueldos[x] < valor_pequeno:
            valor_pequeno = sueldos[x]
            ind_peq = x
        else:
            None    
    for i in range(len(trabajadores)):
        if sueldos[i] > valor_grande:
            valor_grande = sueldos[i]
            ind_gran = i
        else:
            None
            
    for y in range(len(trabajadores)):
        multi *= sueldos[y] 
    geom = (multi) ** (1/10)
     


  
    
    printt(f"El trabajador con el sueldo mayor es {trabajadores[ind_gran]} y su sueldo es de ${mayor_sueldo}")
    printt(f"El trabajador con el sueldo mas pequeño es {trabajadores[ind_peq]} y su sueldo es de ${menor_sueldo}\n")
    printt(f"El promedio de los sueldos es de: {promedio}")
    printt(f"La media geometrica de todos los sueldos es de: {geom}")
    input("enter para continuar!")
    
    
def reporte_sueldos():
    printt("Nombre Empleado\t Sueldo Base\tDescuento Salud\tDescuento AFP\t Sueldo Liquido")
    printt("------------------------------------------------------------------------------")
    for x in range(len(trabajadores)):
        traba = trabajadores[x]
        sueldo_base = sueldos[x]
        desc_salud = sueldos[x]
        desc_fonasa = sueldos[x]
        sueldo_total = sueldo_base - desc_salud - desc_fonasa
        printt(f"{traba}\t\t${sueldo_base}\t\t{desc_salud}\t\t{desc_fonasa}\t\t{sueldo_total}")
        input("enter para continuar...")
        registros.append([traba, sueldo_base, desc_salud, desc_fonasa, sueldo_total])
    printt("Descargar archivo!\n")
    input("enter para continuar!")
    with open('Reporte_archivos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["TRABAJADOR","SUELDO BASE", "DESCUENTO SALUD", "DESCUENTO AFP", "SUELDO_TOTAL"])
        for y in range(len(trabajadores)):
            writer.writerow(registros[y])
    printt("archivo 'reporte_archivos.csv' creado con exito!\n")
    input("Enter para continuar!\n")
    
def salir_menu():
    clear()
    printt("Usted ha salido del sistema....")
    printt("""Codigo Desarrollado por Matias Borquez
          20.814.270-4
          todos los derechos reservados""")
