import math

print("Programa de Matematicas")

def MenuCalculos():
    Menu = '''
    1-  Calculo de Perimetro
    2-  Calculo de Area
    3-  Calculo Suma-Resta de Monomios
    4-  Calculo Multiplicacion-Division de Monomios
    '''

    return print(Menu)

def Calculo_Perimetro(a, b):
    x = int(input("Ingrese el numero de lados que contiene: "))
    lados = int(input("Ingrese los cm los lados contienen: "))

    perimetro = lados * x
    return print("El perimetro es: ", perimetro)

def Calculo_Area(a, b):
    Area = a * b
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
