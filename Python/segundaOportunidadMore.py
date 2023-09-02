import random


print("Inicio")

listaNumeros = []
variableGLobal = random.randint(1, 10)

def Menu(): 
    Menu1 = '''

    1_Volver a intentarlo
    2_Salir

    '''
    return(Menu1)


while True:


    variableUser = int(input("Porfavor ingrese un numero del 1 al 10: "))
    if variableUser == variableGLobal:
        print("¡Ganaste!, ¿quieres volver a intentarlo?")
        listaNumeros.append(variableUser)

        break
    elif variableUser > variableGLobal:
        print("Muy alto")
        listaNumeros.append(variableUser)
    else:
        print("Muy bajo")
        listaNumeros.append(variableUser)
        
print(listaNumeros)
print("Fin")
        

