import math

print("Programa de Matematicas")

def MenuCalculos():
    Menu1 = '''
    1- Calculo con Figuras
    2- Calculo con Numeros y Operaciones
    3-  Calculo de Perimetro
    4-  Calculo de Area
    5-  Calculo Suma-Resta de Monomios
    6-  Calculo Multiplicacion-Division de Monomios
    '''

    return print(Menu1)

def Calculo_Perimetro():
    CantidadLados = int(input("Ingrese el numero de lados que contiene: "))
    lados = int(input("Ingrese los cm los lados contienen: "))
    while lados < 3:
        try:
            lados = int(input("Ingrese el numero de lados que contiene: "))
        except ValueError():
            print("Error")
    perimetro = lados * x   #De un poligono regular
    return print("El perimetro es: ", perimetro)

def Calculo_Area(a, b):
    apotema = a
    Area = Calculo_Perimetro * apotema / 2
    return print("El area es: ",Area)


def Suma_Resta_Monomios():
    print("Cuanto es 4a^2 + 2a^2?")

def Multi_Divis_Monomios():
    print("Cuanto es 4a^2 * 2a^2?")

while True:
    try:
        MenuCalculos()
        Eleccion = int(input("Ingrese su eleccion: "))
        if Eleccion == 1:
            Calculo_Perimetro()

        elif Eleccion == 2:
            Calculo_Area()
    except ValueError():
        print("Error, dato no valido")
