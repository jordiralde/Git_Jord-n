print("inicio")
'''
Calculo:            V= Largo * Ancho * height           (Ancho - (h.x)) * (Largo - (h.x)) = Calcular el maximo volumem
            ¿y para imprimir altura y volumen de esa caja?
'''
print("ingrese valores para ancho y largo de una plancha de carton")
#listas en donde se van a ingresar los dato de altura y volumen
listaV = []
listaH = []
listaMax = []
#Bucle while para que los datos ingresados entren sin error al programa
while True:
    try:
        h=1
        rango = int(input("Ingrese cantidad de iteraciones: "))
        ancho = int(input("El ancho para la plancha de carton: "))
        largo = int(input("El largo para la plancha de carton: "))
        #Se piden los datos iniciales como el rango ancho y largo
        for h in range(rango):
            print("calculo ", (h+2))
            h += 2
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
        print("altura son: ",listaH)
        print(f"la lista es: {listaV}")
        print("El valor más alto encontrado es: ", max(listaV)) #Se usa max() para el valor más alto
        max_area = max(list(listaV))
        
        #list()     
        #zip()      
        
        def hache():
            h = [listaH]
            h = h(listaH) and max_area
            return comparate
        
        comparate = list(zip(listaV, listaH))
        listaMax.append(max_area, )
        print(comparate)
        print(f"los datos son: {listaMax}")
        
        break
    except ValueError:  #exepcion de caracter en datos ingresados
        print("Dato no valiido, reinicio al iteraciones")
        print("---------------------------")

'''
print("ingrese que tan tonto es gordi")
quetantontoesjordan=(int(input()))
list=[]
list.append(quetantontoesjordan)
print("jordan es de tonto: ", quetantontoesjordan)
'''
print("fin")