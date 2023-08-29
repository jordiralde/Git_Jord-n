print("inicio")
def menu():
    menu1= '''
    ************************
    * 1-Suma               *
    * 2-Resta              *
    * 3-Division           *
    * 4-Multiplicacion     *
    * 5-Salir              *
    ************************
    '''
    print(menu1)
    opcionm=int(inut("ingrese una opcion"))
    return(menu1)

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def division(a,b):
    if a == 0 or b == 0:
        print("no se puede dividir por 0")
    else: 
        return a/b

def multiplicacion(a,b): 
    return a*b 

while true: 
    opcion1 = menu1()

    if opcion1 == 5:
        break       
    else: 
        num1=float(input("ingrese el primer numero"))
        num2=float(input("ingrese el segundo numero"))  
        if opcion1 == 1: 
            print(suma(num1,num2))   
        elif opcion1 == 2:
            print(resta(num1,num2))
        elif opcion1 == 3:
            print(division(nume1,num2))
        elif opcion1 == 4: 
            print(multiplicacion(num1,num2))









print("fin")