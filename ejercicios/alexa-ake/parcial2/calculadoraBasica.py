#Alexa Cristel Ake Cuevas
#funciones basicas
def suma(a,b):
    result = a + b


def resta(a,b):
    result = a - b

def multi(a,b):
 return a * b
    
def divi(a,b):
    return a / b 


#menu de opciones
opcion = 0
while(opcion != 5):
    print("\n----Menu de opciones----")
    print("1. Sumar 2 valores")
    print("2. Restar 2 valores")
    print("3. Multiplicar 2 valores")
    print("4. Dividir 2 valores")
    print("5. Terminar programa")
    opcion = int(input("\nSelecciona la opcion deseada [1-5]: "))

    if opcion == 1:
        #Suma de dos numeros
        n1 = float(input("\nIngresa el primer numero a sumar: "))
        n2 = float(input("Ingresa el segundo valor a suma: "))
        print(f"resultado de la suma: {suma(n1,n2)}")
    elif opcion  == 2:
        #resta de dos numeros
        n1 = float(input("\nIngresa el minunedo:"))
        n2 = float(input("Ingresa el sustraendo: "))
        print(f"Diferencia de la resta: {resta(n1,n2)}")
    elif opcion == 3:
        #multiplicacion de dos numeros
        n1 = float(input("\nIngresa el primer factor: "))
        n2 = float(input("Ingresa el segundo factor: "))
        print(f"producto resultante: {multi(n1,n2)}")
    elif opcion == 4:
        #Division de dos numeros
         n1 = float(input("\nIngresa el dividendo: "))
         n2 = float(input("Ingresa el divisor: "))
         print(f"cociente resultante: {divi(n1,n2)}")
    elif opcion == 5:
        #finalizacion del programa
        print("programa finalizado")
        
    else:
        #mensaje de error  por opcion no valida 
        print("!Opcion no valida,intenta nuevamente¡")
