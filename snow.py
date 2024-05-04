import time, os 
while True:
    os.system("cls")
    print("\t\tBienvenido al Hotel Paradise Dreams!!!!!!!!!")
    print("1. Registrar Huésped uwu")
    print("2. Consultar datos de Huésped!")
    print("3. Salir unu")
    try:
        os.system("cls")
        opcion = int(input("ingrese una opcion >.< \n"))
        if opcion == 1:
            os.system("cls")
            print("registro de Huésped")
            nombre = (input("ingrese su nombre :3 \n"))
            while nombre == "":
                nombre =(input("ingrese su fkin nombre! 7u7 \n"))
            direccion = int(input("ingrese su direccion!!!!\n"))
            while direccion == " ":
                direccion = (input("ingrese su fkin direccion >:v \n"))
            numero_reserva = int(input("ingrese su numero de reserva \n"))
            while numero_reserva < 10000 or numero_reserva > 1000:
                numero_reserva = int(input("ingrese su numero de reserva, recuerde que no puede ser menor a 1000, y tampoco mayor a 9999\n"))
            edad = int(input("ingrese su edad uwu \n"))
            while edad <= 18 and edad >= 120:
                print("debe ser mayor de edad we ")
                edad = int(input("ingrese su edad uwu \n"))
            correo = (input("ingrese su correo electronico \n"))
            while '@' not in correo:
                correo = (input("su correo debe poseer almenos un @ :3 \n"))
            acompañante = int(input("ingrese el total de acompañante\n"))
            while acompañante >= 0:
                print("ingrese una cantidad valida uwu ")
                acompañante = int(input("ingrese la cantidad de acompañante po \n"))
                os.system("cls")
        elif opcion == 2:
            print("Datos del Huésped! :33 ")
            print("Su nombre: {nombre}")
            print("Su direccion es: {direccion}")
            print("Su numero de reserva uwu: {numero_reserva}")
            print("Su edad: {edad}")
            print("Su correo electronico!: {correo}")
            print("su total de acompañante: {acompañante}")
            
            
            
    except:
        print("opcion no valida")