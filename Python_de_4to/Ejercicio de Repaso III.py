print("inicio")
while True:
    try:
        cantidad = int(input("cuatnos rectangulos quiere comprar: " ))
        for i in range (cantidad):
            base=int(input(f"ingrese la base de su rectangulo {i+1}: "))
            list = []

            altura=int(input(f"ingrese la altura de su rectangulo {i+1}: "))
            list = []

            area= base*altura
            list = []
            
            

            print(list)
        salir=int(input("ingrese 0 para salir o 1 para volver a comparar"))
        if salir==0:
            break
        elif salir==1:
            print("g")
    except ValueError:
        print("lo siento el valor ingreso es incorrecto, por favor ingresa un numero entero")



"""
            print(f"el area de su rectangulo {i+1} es ",list)  
salir=int(input("presiona 0 para salir o 1 para volver a comparar"))
        if salir==0:
            break
        if salir==1:
            print("ok")
"""



print("fin")