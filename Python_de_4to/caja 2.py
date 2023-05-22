print("inicio")
'''PROGRAMA HECHO POR JORDAN, MateoT
Calculo:            V= Largo * Ancho * height           (Ancho - (h.x)) * (Largo - (h.x)) = Calcular el maximo volumem
            ¿y para imprimir altura y volumen de esa caja?
'''
listaV = [] #listas en donde se van a ingresar los dato de altura y volumen
listaH = []
listaMax = []
def menu(): #se crea la funcion menu para saber si su eleccion es 1 o 2
    print('''
    Ingrese 1 para hacer un calculo
    Ingrese 2 para salir
    ''')
while True: #Bucle while para que los datos ingresados entren sin error al programa
    try:
        menu()#se llama a menu()
        felection = int(input(f"Ingrese..."))   #opciones del menu
        while felection < 1 or felection > 2:#
            menu()
            felection = int(input(f"IngresE..."))
        while felection > 0 and felection < 3:
            if felection == 1:  #valores de una caja de carton
                h=0 
                rango = int(input("Ingrese cantidad de iteraciones: "))#Se piden los datos iniciales
                ancho = int(input("El ancho para la plancha de carton: "))
                largo = int(input("El largo para la plancha de carton: "))
                for h in range(rango):
                    print("calculo ", (h+1))
                    h += 1
                    anchoh = ancho - h              #Ancho - h
                    largoh = largo - h              #Largo - h
                    volumen = anchoh * largoh * h   #Se calcula el volumen
                    print(f"para el ancho: {ancho} - {h} es {anchoh}")
                    print(f"para el largo: {largo} - {h} es {largoh}")
                    print(f"para el area: {anchoh} * {largoh} * {h} = {volumen}")
                    print("---------------------------")
                    listaH.append(h)    #Se imprimen los valores, se almacenan: volumen y h en las listas
                    listaV.append(volumen)
                    #Esto restringe el programa a valores negativos
                    if anchoh and largoh and volumen < 0:
                        print("El codigo no puede llegar a valores negativos :/")
                        break   #Termina el ciclo si el valor llega a negativo
                    #Aca empieza a imprimir el volumen y altura
                    #Se usa max() para el valor más alto           
                for h in range(rango): #Esto hace el calculo del index
                    Altura = listaV.index(max(listaV)) #Con la funcion index() se encuentra la ubicacion de max
                    Altura +=1                      #de una lista, en este caso el maximo es max_area
                for i in range(3):  #Esto solo separa codigo
                    print("")
                print(f"los datos son: [{max(listaV)}] como el maximo volumen y [{Altura}] como la altura de esa caja")
                ''' list()     Aprendi
                    zip()      Aprendi
                    index()    Aprendi'''
                break   #Esto vuelve al primer while para llamar al menu y felection
            else:
                print(f"cerrando...          [{felection}]")
                break
        break
    except ValueError:  #exepcion de caracter en datos ingresados
        print("Dato no valiido, reinicio al menu()")
        print("---------------------------")
print("fin")