print("inicio")
listaVolumen = []
h = 1
while True:
    try:
        largo = int(input("largo de la caja "))
        ancho = int(input("ancho de la caja "))
        rango = int(input("rango: "))
        for i in range(rango):
            print(f"calculo numero {i+1} \n")
            h = h+1
            print(f"el valor de h es {h}")
            
            
            largo2 = largo - 2
            ancho2 = ancho - 2
            
            largo2h = largo2 * h
            ancho2h = ancho2  * h

            volumen = largo2h * ancho2h
            listaVolumen.append(volumen)
            listaVolumen.sort(reverse=True)
            print(f"largo2h= {largo} - 2({largo2}) * {h} = {largo2h}")
            print(f"ancho2h= {ancho} - 2({ancho2}) * {h} = {ancho2h}")
            print(f"volumen= {largo2h} * {ancho2h} = {volumen}")
            print("_______________________________\n")
            if largo2h and ancho2h < 1:
                print("$$$valor negativo$$$")
                break
        print(listaVolumen)
        print(f"El valor maximo es= {max(listaVolumen)}")
        break
    except ValueError:
        print("error")
print("fin")