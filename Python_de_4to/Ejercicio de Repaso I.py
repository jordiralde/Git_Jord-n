print("inicio")

listaArea = []
listaH = []
 
def main(listaArea):
    print ("La lista es ", listaArea)

while True:
    try:
        rango = int(input("Ingrese cantidad de iteraciones: ")) #cantidad de iteraciones
        h=1
        ancho = int(input(f"El ancho para la plancha de carton: "))
        largo = int(input(f"El largo para la plancha de carton: "))
        for h in range(rango):
            print("calculo ", h+1)
            h += 2
            anchoh = ancho - h #ancho - h
            largoh = largo - h #largo - h
            area = anchoh * largoh * h
            print(f"para el ancho: {ancho} - {h} es {anchoh}")
            print(f"para el largo: {largo} - {h} es {largoh}")
            print(f"para el area: {anchoh} * {largoh} * {h} = {area}")
            listaH.append(h)
            listaArea.append(area)
            print(listaArea)
            print("---------------------------")
            if anchoh and largoh and area < 0:      #esto para que no hayan valores negativos
                print("El codigo no puede llegar a valores negativos :/")
                break
        print(listaH)
        main(listaArea)
        max = listaArea[0]
        for x in listaArea:
            if x > max:
                max = x
                
        comparate = zip(listaArea, listaH)
        print("el alto de esa caja es", comparate)
        break
    except ValueError:  #exepcion de caracter en datos ingresados
        print("Dato no valiido, reinicio al iteraciones")
        print("---------------------------")

'''
def de_dos_en_dos():
    i = 2
    while i <= 32:
        print(i)
        i += 2

de_dos_en_dos()

'''



'''
while True:
    
    try:
        print("inicio Programa")
        print("vamos a calcular el area de un triangulo")
        a= float(input("Elija una medida para la base de su triàngulo" ))
        b= float(input("Elija una medidda para la altura de su triàngulo "))
        
        print("el area de su triangulo es:" , a*b/2)
        print("fin Programa")   
    
    except ValueError:
        print("el dato ingresado no es valido etc") 
'''





print("fin")
