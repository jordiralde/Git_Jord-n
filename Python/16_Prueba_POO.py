class Rectangulo():
    #Perimetro es la suma de todos los lados
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        area = self.ancho * self.longitud
        return area
    
    def calcular_perimetro(self):
        perimetro = (self.ancho + self.longitud) * 2
        return perimetro
    
MiRectangulo = Rectangulo(4,5)

print("El area es: ", MiRectangulo.calcular_area())
print("El perimetro es: ", MiRectangulo.calcular_perimetro())
