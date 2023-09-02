print("inicio")
import random

variableGLobal = random.randint(1, 10)
listaNumeros = []

while True:
    variableUsuario = int(input("ingrese del 1 al 10: "))
    if variableUsuario > variableGLobal:
        print("Demasiado alto")
        listaNumeros.append(variableUsuario)
    elif variableUsuario < variableGLobal:
        print("Demasiado bajo")
        listaNumeros.append(variableUsuario)
    else:
        print("Felicidades, Ganaste")
        listaNumeros.append(variableUsuario)
        break

print(listaNumeros)
print("fin")