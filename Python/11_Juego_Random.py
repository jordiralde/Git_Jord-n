print("inicio")
import random

def menu(): #Implementacion por Morena
    menuInicio = '''
    1-  Juego
    2-  Salir
    '''
    return print(menuInicio)

def Juego():
    NumeroRandom = random.randint(1,50)
    NumerosProbados = []
    while True:
        try:
            NumeroJugador = int(input("Ingrese un numero para adivinar: "))
            NumerosProbados.append(NumeroJugador)   #Implementacion por Joshua
            if NumeroJugador == NumeroRandom:
                print("Felicidades, Ganaste")
                break
            elif NumeroJugador > NumeroRandom:
                print("Demasiado alto \n")
            else:
                print("Demasiado bajo\n")
        except ValueError:
            print("error, dato no valido")
    print(NumerosProbados)

while True: #Implementacion por Morena
    menu()
    eleccion = int(input("Ingrese su eleccion: "))
    if eleccion == 1:
        Juego()
    elif eleccion == 2:
        break
    else:
        print("Ingrese 1 o 2")

print("fin")