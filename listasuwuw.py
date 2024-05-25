import os, time 
os.system("cls")
usuarios = []
for x in range(3):
    idUsuario = int(input("\tingrese id de usuario\n"))
    nombre = input("\tingrese nombre de usuario \n")
    correo = input("\tingrese correo\n")
    nivel = int(input("\tingrese su nivel (1 a 100) \n"))


    #diccionario
    usuario = {
        "id" : idUsuario,
        "nombre" : nombre,
        "correo" : correo,
        "nivel" : nivel
         
    }
    usuarios.append(usuario)   
usuarios.remove(usuarios[1])
for i in usuarios:
print(usuarios)
