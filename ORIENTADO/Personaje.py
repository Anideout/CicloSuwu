class Personaje:
                #desde este self, se crean los atributos 
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida


        #asignamos los atributos 
    def atributos(self):
        print(self.nombre, ":", sep="")
        print(f"Fuerza: {self.fuerza}")
        print(f"inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")

    #funcion para subir de nivel! 
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    #saber si sigo con vida 
    def esta_vivo(self):
        return self.vida > 0
    
    #die
    def __morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto....\n")


    
    #funcion para que el daño del enemigo me reste vida con cada estocada 
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    #funcion que ejecuta el daño realizadoo
    def atacar(self, enemigo):
               daño = self.daño(enemigo)
               enemigo.vida = enemigo.vida - daño
               print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
        #llamamos a la funcion esta_vivo, para que diga si vive o no dsp del golpe
               if enemigo.esta_vivo():
    
                    print(f"La vida de: {enemigo.nombre} es {enemigo.vida}")
               else:
                    enemigo.__morir() #con este visualizamos la funcion morir en el enemigo uwu 
    
    
    def get_fuerza(self):
        return self.fuerza
    
    def set_fuerza(self, fuerza):
        if fureza < 0:
            print("Error, has introducido un valor negativo")
        else:
            self.fuerza = fuerza
#datos del personaje, como del enemigo. y las respectivas funciones para que todo funcione xd 
mi_enemigo = Personaje("chopo", 8, 5, 3, 1)
mi_personaje = Personaje("Anideout", 10, 1, 5 ,4) 

class Guerrero(Personaje):
    def __init__(self, nombre,fuerza, inteligencia, defensa, vida, espada):
       
        #super: nos permite llamar a los atributos y metodos de la super clases, sin tener que exhibirla. no hace falta añadir el self, ya que viene explicito dentro del def uwu
        
        super().__init__(nombre,fuerza,inteligencia,defensa,vida)
        self.espada = espada

    def cambiar_arma(self):
        opc = int(input("\tElige un arma!  \n(1) Acero Valyrio: daño 8. \n(2) Matadragones, daño 10\n"))
        if opc == 1:
            self.espada = 8
        elif opc == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecto!")

    def atributos(self):
        super().atributos()
        print("Espada:", self.espada)

    
    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    

    def atributos(self):
        super().atributos()
        print("Libro", self.libro)


    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

anideout = Personaje("Anideout", 20, 15, 10, 100)
guts = Guerrero("Guts", 20, 10, 10, 100, 5)
chopardo = Mago("Chopardo", 20, 15, 10, 100, 5)


def combate(guts,chopardo):
    turno = 0
    while guts.esta_vivo() and chopardo.esta_vivo():
        print("\nTurno", turno)
        print(">>> Accion de ", guts.nombre, ":", sep="")
        guts.atacar(chopardo)
        print(">>>Accion de ", chopardo.nombre, ":", sep="")
        chopardo.atacar(guts)
        turno = turno + 1
    if guts.esta_vivo():
        print("\nHa ganado!", guts.nombre)
    elif chopardo.esta_vivo():
        print("\nHa ganado!", chopardo.nombre)

    else:
        print("\nEmpate xd")

combate(guts, chopardo)

