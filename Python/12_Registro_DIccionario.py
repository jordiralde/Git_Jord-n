print("inicio")
usuarios = {}

def menuInicio():
    menu = '''
    ===========================
        1-  Registrarse
        2-  Iniciar Sesion
        3-  Salir
    ===========================
    '''
    return print(menu)

def registrarse():
    while True:
        try:
            usuarioNuevo = input("Ingrese un nombre para registrarse: ")
            if usuarioNuevo in usuarios:
                print("Ingrese otro usuario, ya esta ocupado \n")
            else:
                global contraseña
                contraseña = input("Ingrese contraseña: ")
                

                repetirContraseña = input("Confirme su contraseña: ")
                if contraseña != repetirContraseña:
                    print("No coinciden las contraseñas")
                else:
                    print("bienvenido " + usuarioNuevo)
                    usuarios[usuarioNuevo] = contraseña
                    break
                break
        except ValueError:
            print("Error, Dato no valido \n")

def iniciar_sesion():
    usuarioNuevo = input("Ingrese un nombre para iniciar sesion: ")
    if usuarioNuevo not in usuarios:
        print("Su usuario no es valido")
        exit(print("fin"))
    contraseña = input("ingrese contraseña: ")

    
    if usuarioNuevo in usuarios and usuarios[usuarioNuevo] == contraseña:
        print("Entro a la NASA")
    else:
        print("Datos incorrectos")

while True:
    menuInicio()
    try:
        eleccion = int(input("ingrese su eleccion: "))
        if eleccion == 1:
            registrarse()

        elif eleccion == 2:
            iniciar_sesion()

        elif eleccion == 3:
            break

        elif eleccion == 4:
            print(usuarios)

        else:
            "Ingrese un dato valido"
        
    except ValueError:
        print("Error, dato no valido \n")

print("fin")
