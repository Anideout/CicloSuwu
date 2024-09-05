#creando personaje 
class personaje:
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    #estadisticas bases del personaje 
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    #definiendo atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
    
    #funcion para subir de nivel 
    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa 

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0 
        print(f"{self.nombre} ha muerto....")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        printt(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        printt("La vida de", enemigo.nombre, "es", enemigo.vida)


mi_personaje = personaje("anideout", 10, 1, 5, 100)
mi_enemigo = personaje("Enemy estando", 8, 5, 3, 100)
printt(mi_personaje.daño(mi_enemigo))
mi_enemigo.atributos()
