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
#---------------------------------------------------CLASES------------------------------------------------------
class Personaje:
    ''' 
        Esta clase va a ser la maqueta de los personajes, los personajes cuentan con:
        Vida, Armadura y Fuerza
                                    Los personajes pueden:
        Atacar
        Defender
        Comer
    '''

    vida = 50   #Vida Default
    velocidad = 5
    
    def __init__(self, armadura, fuerza, nombre) -> None:
        self.armadura = armadura
        self.fuerza = fuerza
        self.nombre = nombre
        
    def Defender(self):
        
        Pdef = self.defensa = self.vida * self.armadura
        return print(Pdef)

    def Atacar(self):
        self.ataque = self.fuerza * self.velocidad
        return print("el ataque inflingido es: ",self.ataque)

    def Comer(self):
        self.vida = 50
        return print("Se restauro la vida")
    
#---------------------------------------------------------------------------------------------------------------

class Auto:     #Por convencion la primera letra es en mayuscula
    ''' Documentacion de la funcion de la clase '''

    vida = 500
    velocidad = 0
    ruedas = 4
    color = 'rojo'
    
    def __init__(self, color, aceleracion, nombre) -> None:
        self.color = color
        self.nombre = nombre
        self.aceleracion = aceleracion

    def Subirse(self):
        return print("---------------Estas en el auto---------------")
        
    def Bajarse(self):
        return print("---------------Bajaste del auto---------------")
        
    def Acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion
        return print("El auto acelero, la velocidad es: ", self.velocidad)

    def Frenar(self):
        v = self.velocidad 
        if v > 0:
            v -= self.aceleracion
            print(v)
        self.velocidad = v
        return print("freno, la velocidad es ",v)

#--------------------------------------------------FUNCIONES----------------------------------------------------
PersonajeJugador = Personaje(50, 50, 'Jordan')
AutoDeJugador = Auto('rojo', 50, 'Auto del Jugador')

def AccionesDeJugador():
    MenuOpciones = ('''
            Acciones Del Jugador
    1-  Acciones del auto
    2-  Defenderse
    3-  Atacar
    4-  Comer
    ''')
    return print(MenuOpciones)

def AccionesDeJugadorParaAuto():
    MenuAuto = ('''
            Acciones Para El Auto
    1-  Subirse
    2-  No hacer nada
    3-  Pegarle
    ''')
    MenuEnAuto = '''
    1-  Bajar
    2-  Acelerar
    3-  Frenar
    '''
    while True:
        try:
            print(MenuAuto)
            Eleccion = int(input("Ingrese acciones en el auto: "))

            if Eleccion == 1:
                while True:
                    AutoDeJugador.Subirse()
                    print("la velocidad es: ", AutoDeJugador.velocidad)
                    print(MenuEnAuto)

                    EleccionEnAuto = int(input("Ingrese acciones en el auto: "))

                    if EleccionEnAuto == 1 and AutoDeJugador.velocidad == 0:
                        AutoDeJugador.Bajarse()
                        break

                    elif EleccionEnAuto == 1 and AutoDeJugador.velocidad > 0:
                        print("no puede bajarse, reduzca la velocidad a 0")
                        
                    elif EleccionEnAuto == 2:
                        AutoDeJugador.Acelerar()
                    elif EleccionEnAuto == 3:
                        AutoDeJugador.Frenar()
                    else:
                        print("No hizo nada")


            elif Eleccion == 2:
                print("No esta pasando nada")
                break

            elif Eleccion == 3:
                PersonajeJugador.Atacar()
                print(f"Golpeaste al [{AutoDeJugador.nombre}], la vida del [{AutoDeJugador.nombre}] es: ", Auto.vida - Personaje)
                print("Otro golpe?")

                while True:
                    SistemaDeAtaque = int(input("1 para atacar, otro para hacer nada: "))
                    if SistemaDeAtaque == 1:
                        print(f"Otro golpe, la vida del [{AutoDeJugador.nombre}] es: ", AutoDeJugador.vida)
                    else:
                        print("No hizo nada")
                        break

            else:
                print(MenuAuto)
                print("Elija una de las opciones")
        except ValueError:
            print("dato no valido")


#Sistema de ataque funciona asi


#Personaje.vida - PersonajeJugador.atacar

#--------------------------------------------------------------------------------------------------------------
while True:
    AccionesDeJugador()
    Eleccion = int(input("Eleccion "))
    if Eleccion == 1:
        AccionesDeJugadorParaAuto()
    elif Eleccion == 2:
        PersonajeJugador.Defender
        print("te defendiste de algo")
    elif Eleccion == 3:
        PersonajeJugador.Atacar
        print("Atacaste")
    elif Eleccion == 4:
        PersonajeJugador.Comer
        print("Comiste")
    else:
        break

print("fin")