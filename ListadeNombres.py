#Actividad 1 
import os, time 
# os.system("cls")
# def main():
#     nombres = []
#     for i in range(3):
#         nombre = input("ingrese un nombre: \n")
#         nombres.append(nombre)
        
#     nombre_maslargo = max(nombres, key=len)
#     print(f"El nombre más largo de los 3 ingresados es: {nombre_maslargo}")
    
# if __name__ == "__main__":
#     main()
        
#actividad 2 
# os.system("cls")
# def main():
    
#     nombres = []
#     apellidos = []
#     for i in range(3):
#         nombre = input("ingrese un nombre: \n")
#         apellido = input("ingrese un apellido!: \n")
#         nombres.append(nombre)
#         apellidos.append(apellido)
#         os.system("cls")
        
#         for nombre, apellido in zip(nombres, apellidos ):
#             print(f"{nombre} {apellido}")
# if __name__ == "__main__":
#     main()
    
    def main():
        nombres = []
        while True:
            nombre = input("ingrese un nombre \n")
            nombres.append(nombre)
            pregunta = input("desea ingresar otro usuario? (si/no)").lower()
            if pregunta != "si" and pregunta != "SI":
                break
            nombre_menor = min(nombre, key=len)
            nombre_borrar = (nombre_menor)
            print(f"se ha eliminado el '{nombre_menor} con menos caracteres ingresados uwu ")
            if __name__ == "__main__":
            main()