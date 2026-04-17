#Funciones basicas 
def suma (a,b):
    result = a  + b
    return result

def resta (a,b):
    result = a - b
    return result 

def multi (a,b):
    result = a * b
    return result 

def division (a,b):
    return a/b
    #menu de opciones
opcion = 0  
while(opcion != 5):
    print("---- Menu de opciones ----")
    print("1. Sumar 2 valores")
    print("2. Restar 2 valores")
    print("3. Multiplicar 2 valores")
    print("4. Dividir 2 valores")
    print("5. Terminar programa")
    opcion = int(input("\nSelecciona la opcion deseada [1-5]: "))

if opcion == 1:
    #suma de dos numeros 
    n1 = float (input ("\nIngresa el primer numero a sumar: "))
    n2 = float (input ("\nIngresa el segundo valor a sumar "))
    print(f"diferencia de la suma: {suma(n1,n2)}")

elif opcion == 2:
    #resta de dos numeros
    n1 = float (input ("\nIngresa el minuendo: "))
    n2 = float (input ("\nIngresa el sustraendo "))
    print(f"cociente de la resta:{resta(n1,n2)} ")

elif opcion == 3:
    #multiplicacion de dos numeros 
    n1 = float (input ("\nIngresa el primer factor: "))
    n2 = float (input ("\nIngresa el segundo factor "))
    print(f"producto resultante: {multi(n1,n2)}")

elif opcion == 4:
    #division de dos numeros 
    n1 = float (input ("\nIngresa el dividiendo: "))
    n2 = float (input ("\nIngresa el divisor: "))
    print(f"cociente resultado: {division(n1,n2)}")
elif opcion == 5:
    #finalizacion del programa 
    print("programa finalizado...")
    

else:
    # mensaje de error por opcion no valida 
    print("opcion no valida, intenta de nuevamente")

