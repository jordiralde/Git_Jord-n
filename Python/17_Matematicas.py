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
    while True :
        try:
            CantidadLados = int(input("Ingrese el numero de lados que contiene: "))
            if CantidadLados < 3:
                print("No se puede")
                break
            CmDeLados = int(input("Ingrese los cm los lados contienen: "))
            perimetro = CmDeLados * CantidadLados   #De un poligono regular

            break
        except ValueError():
            print("Error")
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
    MenuCalculos()
    try:
        Eleccion = int(input("Ingrese su eleccion: "))
        if Eleccion == 1:
            #Calculo_Figuras()
            print()

        elif Eleccion == 2:
            #Calculo_NumeroOperaciones()
            print()
            
        elif Eleccion == 3:
            Calculo_Perimetro()

    except ValueError():
        print("Error, dato no valido")
