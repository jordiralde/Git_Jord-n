class PruebaRectangulos():

    def __init__ (self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calculararea(self):
        area = self.longitud * self.ancho
        return print("el area es ", area)
    
    def calculorperimetro(self):
        perimetro = (self.longitud + self.ancho) * 2
        return print("El perimetro es ", perimetro)
    
Mirectangulo = PruebaRectangulos(4, 5)

Mirectangulo.calculararea()
Mirectangulo.calculorperimetro()