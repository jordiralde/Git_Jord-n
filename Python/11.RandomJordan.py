print("inicio")
import random
NumerosProbados = []
NumeroRandom = random.randint(1,50)

while True:
    try:
        NumeroJugador = int(input("ingrese valor: "))
        if NumeroRandom == NumeroJugador:
            print("Felicidad")
            NumerosProbados.append(NumeroJugador)
            break
        elif NumeroJugador > NumeroRandom:
            print("alto")
            NumerosProbados.append(NumeroJugador)
        else:
            print("bajo")
            NumerosProbados.append(NumeroJugador)
    except ValueError:
        print("Error no valido")

print(NumerosProbados)
print("fin")