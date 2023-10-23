class Auto:     #Por convencion la primera letra es en mayuscula
    ''' Documentacion de la funcion de la clase '''

    ruedas = 4
    color = 'rojo'
    
    def __init__(self, color, aceleracion) -> None:
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 5
    
    def aceleracion(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v > 0:
            v = 0
        self.velocidad = v
        return v

obj1 = Auto('Rojo', 50)
print(f"La cantidad de Ruedas es: {obj1.ruedas}")
print(f"El color del auto es: {obj1.color}")
print("La veocidad es: ", obj1.velocidad)
print("La velocidad del auto es ", obj1.aceleracion)
print("El auto freno, la velocidad es: ", obj1.frenar)

obj2 = Auto('Rojo', 30)

ac = obj1.aceleracion - obj2.aceleracion