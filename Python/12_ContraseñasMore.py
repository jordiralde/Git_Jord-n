#Generador de contraseñas aleatorias con frases mnemotecnicas, actividad de hackatoon 2023
#Que Muestre contraseñas generadas y que sean comparadas para verificar la eficacia

#Hacer una IA que automatice el ultimo paso, la contraseña es de datos recolectados
import random
print("inicio")

print('''
    Reglas mnemotecticas
    1-  Técnica de las Iniciales
    Esta estrategia consiste en construir una palabra con la primera letra de cada palabra de una lista.
    ''')
def menu():
    MenuInicio = '''
    1-  Obtener contraseña aleatoria
    2-  Mostrar contraseñas generadas
    3-  Salir
    '''
    return(print(MenuInicio))

ContraseñasGuardadas = []

while True:
    try:
        menu()
        eleccion = int(input("Ingrese su eleccion"))
        if eleccion == 1:
            print("Ingrese sus datos personales")
            contraseñaGenerada = random.randrange('a','b','c')
            ContraseñasGuardadas.append(contraseñaGenerada)
            print(contraseñaGenerada)

        elif eleccion == 2:
            print(ContraseñasGuardadas)

        else:
            print("acuerdese de anotar en un papel su contraseña!")
            break
    except ValueError:
        print("Error")


print("fin")