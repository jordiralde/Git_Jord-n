class Auto:
    ''' Documentacion de la funcion de la clase '''

    ruedas = 4
    
    def __init__(self, color, aceleracion) -> None:
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
    
    def aceleracion(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v > 0:
            v = 0
        self.velocidad = v

print(Auto)