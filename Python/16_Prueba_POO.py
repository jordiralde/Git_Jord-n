class Rectangulo():
    #Perimetro es la suma de todos los lados
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
            #self.area = self.ancho * self.longitud
            #return print("El area es: ",self.area)
        area = self.ancho * self.longitud
        #return print("El area es: ",area)
        return area
    
    def calcular_perimetro(self):
        perimetro = (self.ancho + self.longitud) * 2
        return print("El perimetro es: ", perimetro)
    
MiRectangulo = Rectangulo(4,5)

    #print(MiRectangulo.calcular_area())
print("El area es: ", MiRectangulo.calcular_area())
MiRectangulo.calcular_area()
MiRectangulo.calcular_perimetro()