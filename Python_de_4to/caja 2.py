print("inicio")
'''PROGRAMA HECHO POR JORDAN, MateoT
Calculo:            V= Largo * Ancho * height           (Ancho - (h.x)) * (Largo - (h.x)) = Calcular el maximo volumem
            ¿y para imprimir altura y volumen de esa caja?
'''
#listas en donde se van a ingresar los dato de altura y volumen
listaV = []
listaH = []
listaMax = []
#se crea la funcion menu para saber si su eleccion es 1 o 2
def menu():
    print('''
    Ingrese 1 para hacer un calculo
    Ingrese 2 para salir
    ''')
while True: #Bucle while para que los datos ingresados entren sin error al programa
    try:
        menu()#se llama a menu()
        felection = int(input(f"Ingrese..."))   #opciones del menu
        while felection > 0 and felection < 3:
                if felection == 1:
                        #valores de una caja de carton
                        h=0 
                        rango = int(input("Ingrese cantidad de iteraciones: "))
                        ancho = int(input("El ancho para la plancha de carton: "))
                        largo = int(input("El largo para la plancha de carton: "))
                        #Se piden los datos iniciales como el rango ancho y largo
                        for h in range(rango):
                            print("calculo ", (h+1))
                            h += 1
                            anchoh = ancho - h              #Ancho - h
                            largoh = largo - h              #Largo - h
                            volumen = anchoh * largoh * h   #Se calcula el volumen
                            print(f"para el ancho: {ancho} - {h} es {anchoh}")
                            print(f"para el largo: {largo} - {h} es {largoh}")
                            print(f"para el area: {anchoh} * {largoh} * {h} = {volumen}")
                            #Se imprimen los valores, se almacenan: volumen y h en las listas
                            listaH.append(h)
                            listaV.append(volumen)
                            print("---------------------------")
                            #Esto restringe el programa a valores negativos
                            if anchoh and largoh and volumen < 0:
                                print("El codigo no puede llegar a valores negativos :/")
                                break   #Termina el ciclo si el valor llega a negativo
                        #Aca empieza a imprimir el volumen y altura
                        max_area = max(listaV)  #Se usa max() para el valor más alto
                        while True:             #Esto hace el calculo del index
                            for h in range(rango):
                                Altura = listaV.index(max_area) #Con la funcion index() se puede encontrar la ubicacion de un numero especifico
                                Altura +=1                      #de una lista, en este caso el maximo es max_area
                            break
                        for i in range(3):  #Esto solo separa codigo
                            print("...")
                        print(f"los datos son: [{max_area}] como el maximo volumen y [{Altura}] como la altura de esa caja")#Se imprime la caja
                        #list()     Aprendi
                        #zip()      Aprendi
                        #index()    Aprendi
                        break   #Esto vuelve al primer while para llamar al menu y felection
                else:
                    print(f"cerrando...          [{felection}]")
                    break
        break
    except ValueError:  #exepcion de caracter en datos ingresados
        print("Dato no valiido, reinicio al menu()")
        print("---------------------------")
print("fin")