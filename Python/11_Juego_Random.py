print("inicio")
import random

def menu():
    menuInicio = '''
    1-  Random
    2-  Salir
    '''
    return print(menuInicio)

def randomF():
    NumeroRandom = random.randint(1,50)
    NumerosProbados = []
    while True:
        try:
            NumeroJugador = int(input("Ingrese un numero para adivinar: "))

            if NumeroJugador == NumeroRandom:
                print("Felicidades, Ganaste")
                NumerosProbados.append(NumeroJugador)
                break
            elif NumeroJugador > NumeroRandom:
                print("Demasiado alto \n")
                NumerosProbados.append(NumeroJugador)
            else:
                print("Demasiado bajo\n")
                NumerosProbados.append(NumeroJugador)
        except ValueError:
            print("error, dato no valido")
    print(NumerosProbados)

while True:
    menu()
    eleccion = int(input("ingrese su eleccion: "))
    if eleccion == 1:
        randomF()
    elif eleccion == 2:
        break
    else:
        print("Ingrese")
print("fin")