class rectangulo():
    
    #Esta clase realizara el calculo del area y del perimetro de un rectangulo

    def __init__(self, longitud, ancho) -> None:
        self.longitud = longitud
        self.ancho = ancho

    def calculo_area(self):
        self.area = self.longitud * self.ancho
        return print(f"El area del rectangulo es: {self.area}")

    def calculo_perimetro(self):
        self.perimetro = (self.longitud * 2) + (self.ancho * 2)
        return print(f"El perimetro del rectangulo es {self.perimetro}")
    
MiRectangulo = rectangulo(3, 4)

MiRectangulo.calculo_area() 
MiRectangulo.calculo_perimetro()
