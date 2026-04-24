#funciones basicas 
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multi(a,b):
    return a * b

def division(a,b):
    return a / b
#menu de opciones 
opcion = 0
while(opcion != 5):
    print("----Menu de opciones ----")
    print("1. sumar 2 valores")
    print("2. restar 2 valores")
    print("3. multiplicar 2 valores")
    print("4. Dividir 2 valores")
    opcion = int(input("\nselecciona la opcion deseada [1-5]: "))

    if opcion == 1:
        #suma de dos numeros
        n1 = float( input("\nIngresa el numero a sumar: "))
        n2 = float(input("ingresa el segundo valor a sumar "))
        print(f"resultado e la suma: {suma(n1,n2)}")
    elif opcion == 2:
        n1 = float( input("\nIngresa el numero a miniendo: "))
        n2 = float(input("ingresa el segundo valor a sustraendo "))
        print(f"cociente ce la resta: {resta(n1,n2)}")
        #resta de dos numeros 
    elif opcion == 3:
        n1 = float( input("\nIngresa el numero a primer factor: "))
        n2 = float(input("ingresa el segundo valor a segundo factor "))
        print(f"producto resultante: {multi(n1,n2)}")
        #multiplicacon de dos numeros
    elif opcion == 4:
        n1 = float( input("\nIngresa el numero a dividiendo: "))
        n2 = float(input("ingresa el segundo valor a divisor "))
        print(f"cociente resultante: {division(n1,n2)}")
      #divsion de dos numeros
    elif opcion == 5:
        n1 = float( input("\nIngresa el numero a sumar: "))
        n2 = float(input("ingresa el segundo valor a sumar ")) 
        print("programa finalizado...")
        #finalizar el programa
    else:
        #mensaje de error por opcion no valida
        print("opcion seleccionada no valida, intenta nuevamente!")