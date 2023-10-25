'''
Actividad de programación orientada a objetos de a dos
Desarrollar un código que contenga dos clases con sus atributos y métodos. 
Luego crear las instancias y simular una interacción entre objetos de diferentes clases.
Pueden ampliar o agregar funcionalidades a dichas clases
     O
    /|\
    / \
'''
#1- Responsabilidad única. ...          S
#2- Abierto/Cerrado                     O
#3- Sustitución de Liskov. ...          L
#4- Segregación de interfaz. ...        I
#5-  Inversión de dependencia.          D

print("inicio")


class Personaje:
    ''' 
        Esta clase va a ser la maqueta de los personajes, los personajes cuentan con:
        Vida, Armadura y Fuerza
                                    Los personajes pueden:
        Atacar
        Defender
        Saludar
        Comer
    '''

    vida = 50   #Vida Default
    
    def __init__(self, armadura, fuerza, nombre) -> None:
        self.armadura = armadura
        self.fuerza = fuerza
        self.nombre = nombre
        
    def Defender(self):
        self.defensa = self.vida * self.armadura

    def Atacar(self):
        self.ataque = self.fuerza * self.velocidad

    def Comer(self):
        self.vida = 50
        return print("Se restauro la vida")
    

#--------------------------------------------------------------------------------------------------------------

class Auto:     #Por convencion la primera letra es en mayuscula
    ''' Documentacion de la funcion de la clase '''

    ruedas = 4
    color = 'rojo'
    
    def __init__(self, color, aceleracion, nombre) -> None:
        self.color = color
        self.nombre = nombre
        self.aceleracion = aceleracion
        self.velocidad = 5
    
    def subirse(self):
        if AccionesDeJugadorParaAuto() == True:
            return print("Estas en el auto")
        
    def bajarse(self):
        if AccionesDeJugadorParaAuto() == True:
            return print("Bajaste en el auto")
        
    def acelerar(self):
        if AccionesDeJugadorParaAuto() == True:
            self.velocidad = self.velocidad + self.aceleracion
            return print("El auto acelero, la velocidad es", self.velocidad)

    def frenar(self):
        if AccionesDeJugadorParaAuto() == True:
            v = self.velocidad - self.aceleracion
            if v > 0:
                v = 0
            self.velocidad = v
            return v

#--------------------------------------------------------------------------------------------------------------
PersonajeJugador = Personaje(50, 50, 'Jordan')
AutoDeJugador = Auto('rojo', 50, 'Auto de Jugador')

def AccionesDeJugador():
    MenuOpciones = ('''
            Acciones Del Jugador
    1-  Auto
    2-  Defenderse
    3-  Atacar
    4-  Comer  
    ''')
    return print(MenuOpciones)

def AccionesDeJugadorParaAuto():
    MenuAuto = ('''
            Acciones Para El Auto
    1-  Subirse
    2-  Bajar
    3-  Acelerar
    4-  Frenar
    5-  No hacer nada
    ''')
    return print(MenuAuto)

#--------------------------------------------------------------------------------------------------------------


while True:
    for i in range(5):
        AccionesDeJugador()
        Eleccion = int(input("Eleccion "))
        if Eleccion == 1:
            AccionesDeJugadorParaAuto()
            Eleccion = int(input("Ingrese su eleccion para el auto "))
        elif Eleccion == 2:
            print(PersonajeJugador.nombre)

    break

print("fin")