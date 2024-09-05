import time
from os import system, name
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def menu():
    print("Bienvenido al exitoso juego Call of Honor!!!!! donde jugaras por tu honor o algo así ")
    print("-------Sistema de Gestion de Jugadores -  **Epic Quest** -------")
    print("1.registrar jugador! ")
    print("2. Consultar datos de jugador ")
    print("3. SALIR u.u")

def nombre():
    clear()
    nombre = input("Ingrese su nombre por favor!\n")
    while nombre == "" or nombre == " ":
        nombre = input("Ingrese su nombre de nuevo por favor!\nRecuerde que no puede venir el espacio vacio!\n")
    return nombre
        
def ID():  
    clear()
    banID = True
    while banID:
        id_jugador = int(input("Ingrese su id por favor uwu recuerde que tiene que ser entre 10000 y 100000\n"))
        if id_jugador > 9999 and id_jugador < 100000:
            print("id registrado con exito!\n")
            banID = False
        else:
            clear()
            print("\nSu id no ha podido ser registrado, recuerde que tiene que ser entre el rango de 10000 y 100000\n")
    return id_jugador

def nivel():
    clear()
    banNIvel = True
    while banNIvel:
        nivel = int(input("INgrese su nivel por favor!\n"))
        if nivel >= 1 and nivel <= 101:
            print("Su nivel de usuario ha sido registado con exiton\n")
            banNIvel = False
        else:
            clear()
            print("Ingrese nuevamente por favor!\n")
    return nivel

def correo():
    clear()
    correo = input("Ingrese su correo electronico por favor!\n")
    while '@' not in correo:
        correo = input("Ingrese su correo electronico bien por favor!\n")
def rol():
    banRol = True
    while banRol:
        rol_jugador = input("Ingrese su rol en el juego!: Objective, Slayer, Support, anchor\n")
        if rol_jugador == "Objective" or rol_jugador == "objective" or rol_jugador == "Slayer" or rol_jugador == "slayer" or  rol_jugador == "Support" or rol_jugador == "support" or rol_jugador == "Anchor" or rol_jugador == "anchor":
            banRol = False
            print("Rol ingresado con exito!\n")
        else:
            print("Su rol no ha podido ser registrado, ya que lo ingresaste mal\n")